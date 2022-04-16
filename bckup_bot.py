# -*- encoding: utf-8 -*-
import mysql.connector
from flask_runner import Runner
import os
from clients_database import Data_base_manager
import win32com.client as win32

runner = Runner()


class bot_database:
    def __init__(self):
        self.auctions_db = Data_base_manager('auctions_db', 'auctions',
                                             ['site', 'category', 'price', 'url', 'local'])


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


clientsDB = Data_base_manager('auctions_db', 'clients',
                              ['client_name', 'client_local'])

places = clientsDB.select_distinct('client_local', '')
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
        if client[2] == new:
            clients_to_send.append(client[1])
    clients_to_send = ', '.join(clients_to_send)
    if len(news[new]) > 0:
        for n in news[new]:
            table += f"""
            <tr>
                <td>{n[0]}</td>
                <td>{n[1]}</td>
                <td>{n[2]}</td>
                <td>{n[3]}</td>
                <td>{n[4]}</td>
            </tr>
        """

        content += f"""<h2> Clientes interessados: {clients_to_send} <br>({len(news[new])}) LUGAR: {new}<h2/>
    <table style="width:100%">
            <tr>
                <th>Site</th>
                <th>Categoria</th>
                <th>Preço</th>
                <th>Url</th>
                <th>Lugar</th>
            </tr>
            {table}
            </table>
    """

style = """<style>
    table, th, td {
  border:1px solid black;
}
h1{ color: red
}
<style/>"""
email.HTMLBody = body = f"""{style}
<body>
<h1> NOVOS LEILÕES ENCONTRADOS </h1>
{content}
<bddy/>
"""

print('email enviado')
