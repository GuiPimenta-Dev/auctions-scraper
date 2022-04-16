# -*- encoding: utf-8 -*-
import mysql.connector
from flask_runner import Runner
import os
from clients_database import Data_base_manager
import win32com.client as win32






def check_db(city, new_data):
    auctions_db = Data_base_manager('auctions_db', 'auctions',
                                    ['site', 'category', 'price', 'url', 'local'])
    # TRATAR NOVOS DADOS
    tuples = []
    for data in new_data['data']:
        data.pop('description')
        data.update({'local': city})
        tuples.append(tuple(data.values()))

    current_datas = auctions_db.select_city(city)
    new_auctions = []
    for new in tuples:
        if new not in current_datas:
            print(f'NOVO LEILÃO: {new}')
            auctions_db.insert_db(new)
            new_auctions.append(new)

    for current in current_datas:
        if current in tuples:
            print(f'LEILÃO ATUAL:  {current}')
        elif current not in tuples:
            print(f'LEILÃO ANTIGO : {current}')
            auctions_db.delete_db(
                f'site = "{current[0]}"AND category = "{current[1]}" AND price = "{current[2]}" AND url = "{current[3]}" AND local = "{current[4]}"')

    return new_auctions

def filter_and_send_email():
    runner = Runner()
    clientsDB = Data_base_manager('auctions_db', 'clients',
                                  ['client_name', 'client_local'])

    places = clientsDB.select_distinct('client_local', '')
    clients = clientsDB.show_table()

    news = {}
    for place in places:
        place = place[0]
        #GET THE NEW DATA
        data = runner.run_robots(place)

        # CHECK THE DATABASE
        result = check_db(place,data)
        print(result)
        news[place] = result


    if len(result)>0:
        print('mandando email..')
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)
        email.To = 'gabrielpimenttas@gmail.com'
        email.Subject = 'Novos Leilões'

        content = ''

        for new in news.keys():
            table = ''
            clients_to_send = []
            for client in clients:
                if client[1] == new:
                    clients_to_send.append(client[0])
            clients_to_send = ', '.join(clients_to_send)
            if len(news[new]) > 0:
                for n in news[new]:
                    table += f"""
                    <tr>
                        <td>{n[0]}</td>
                        <td>{n[1]}</td>
                        <td>{n[2]}</td>
                        <td>{n[3]}</td>                        
                    </tr>
                """

                content += f"""<p style="font-size: 25px;
    font-weight: 400;"> Clientes interessados: {clients_to_send} <br>({len(news[new])}) Novos leilões <br> LUGAR: {new}<p/>
           <section style ="box-shadow: 0 5px 8px rgb(194, 194, 194);
    max-height: 500px;
    margin: 50px;
    display: block;
    overflow: auto;">
                <table style="box-shadow: 0 5px 8px rgb(194, 194, 194);
    border-collapse: collapse;
    text-align: center;
    width: 100%;
    margin: auto;">
                    <thead style="position: sticky;
    top: 0;
    background-color: white;
    box-shadow: 0 5px 8px rgb(194, 194, 194);
    padding: 15px;
    border-top-left-radius: 50px;
    border-top-right-radius: 50px;
    background-color: rgb(230, 230, 230);
    line-height: 60px;">
                        <tr>
                            <th>Site</th>
                            <th>Categoria</th>
                            <th>Preço</th>
                            <th>Url</th>                            
                        </tr>
                    </thead>
                    <tbody style="line-height: 50px">
                        
                            {table}
                        
                    </tbody>
                    </table>
                </section>
            """


        css = """tbody tr:nth-child(even){
    background-color: #42d699d5;
    color: rgb(0, 0, 0);
}"""
        email.HTMLBody = f"""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        
    </style>
</head>
<body>
    <container style = "font-family: 'Roboto', sans-serif;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-content: center;
    justify-content: center;
    background-color: rgb(255, 255, 255)">
    <h1 style = "font-weight: 700;
    font-size: 45px;
    text-transform: uppercase;
    text-align: center;"> NOVOS LEILÕES </>
        {css}
    </container>
</body>
</html>
        """
        email.Send()
        print('email enviado')

filter_and_send_email()