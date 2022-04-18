import json
from urllib.parse import urlencode
from clients_database import Data_base_manager, client_check, create_table

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import urllib

import mysql.connector
from flask_runner import Runner

app = Flask(__name__)
CORS(app)
runner = Runner()
auctions_db = Data_base_manager('auctions_db', 'auctions',
                                ['site','category', 'price', 'url', 'local'])

clients_db = Data_base_manager('auctions_db', 'clients',['client_name','client_local'])






@app.route('/home')
def home():
    return 'Home'


@app.route("/")
def run_robots():
    state_city = request.args.get('state_city', '')
    try:
        data = runner.run_robots(state_city)

    except Exception as e:
        data = str(e)
    print(data)
    return data


@app.route("/register/<name>/<local>")
def register_db(name, local):

    try:
        name = f'{name.capitalize()}'
        local = f'{local.capitalize()}'
        if client_check(clients_db, (name, local)):
            clients_db.insert_db([name,local])

            print(local)

            current_places = auctions_db.select_distinct('local','')
            print(current_places)
            if (local,) in current_places:
                print('Já tem')

            else:
                print('nao tem')
                datas = runner.run_robots(local)
                print('fim')
                print(datas)
                for data in datas['data']:
                    auctions_db.insert_db([data['site'],data['category'], data['price'], data['url'], local])


        return 'sucesso'
    except:
        return 'falha'




@app.route("/clients_auction/<local>")
def show_clients_auctions(local):
    db = auctions_db.select_city(local)
    db_list = []
    for row in db:
        db_list.append(row)
    return jsonify(db_list)



@app.route("/clients")
def show_clients():
    clients_table = clients_db.show_table()
    clients_json = []
    for client_tuple in clients_table:
        client_list = []
        for client in client_tuple:
            client_list.append(client)
        clients_json.append(client_list)
    return jsonify(clients_json)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
