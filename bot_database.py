# -*- encoding: utf-8 -*-
import mysql.connector
from flask_runner import Runner
import os
from clients_database import Data_base_manager
import win32com.client as win32

import schedule
import time


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
    # ALL DIFERENT PLACES IN DB
    places = clientsDB.select_distinct('client_local', '')

    # CLIENTS TUPLES
    clients = clientsDB.show_table()

    news = {}
    for place in places:
        place = place[0]
        # GET THE NEW DATA
        data = runner.run_robots(place)

        # CHECK THE DATABASE
        result = check_db(place, data)
        print(result)
        news[place] = result
    keep = False
    for new in news.keys():
        if news[new]:
            keep = True

    if keep:
        print('mandando email..')
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)
        email.To = 'guialvespimenta27@gmail.com'
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
                       <tbody>
                            <tr>
                                <td>{n[0]}</td>
                                <td>{n[1]}</td>
                                <td>{n[2]}</td>
                                <td>{n[3]}</td>                        
                            </tr>
                        </tbody>
                        
                    """

                content += f"""<p> Clientes interessados: {clients_to_send}. <br>{len(news[new])} Novos leilões <br> LUGAR: {new}<p/>
               
                        <table >
                            <thead style="font-size:25px" > 
                                <tr style="background-color: #35CE8D";>
                                    <th style="font-size: 25px">SITE</th>
                                    <th>CATEGORIA</th>
                                    <th>PREÇO</th>
                                    <th>URL</th>                            
                                </tr>                    
                            </thead>
                                {table}
                        </table>
                    
                """

        css = """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

            body{
                font-family: Roboto;
                background-color: rgb(241, 241, 241);
            }
            h1{
                font-size: 60px;
                text-transform: uppercase;
                text-align: center;
            }
             p{
                font-size: 25px;
            }
            table{
                width: 80%;
                margin: auto;
                box-shadow: 10px 10px 18px rgb(194, 194, 194);
                border-collapse: collapse;
                text-align: center;  
                background-color: white; 
               
                
            }
            thead{
                line-height: 50px;
                font-size: 25px;
                box-shadow: 0 5px 8px rgb(163, 163, 163);
                background-color: #35CE8D;
                color: white;
                
            }
            tbody tr{
                line-height: 50px;
            }
            tbody tr:nth-child(even){
                background-color: rgb(243, 243, 243);
            }
            </style>
        """
        email.HTMLBody = f"""
        
                  {css}      
        
    </head>
    
    <body>
        
        <h1> SCHEDULE LEILÃO </h1>
            {content}
        <br><br>
    </body>
            """
        email.Send()
        print('email enviado')




filter_and_send_email()

schedule.every().day.do(filter_and_send_email)


while True:
    schedule.run_pending()
    time.sleep(1)

