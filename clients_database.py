import mysql.connector
import  win32com.client as win32


class Data_base_manager:
    def __init__(self, database, table, columns):
        self.cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='MrWh1t32',
            database=database
        )
        self.table = table
        self.keys = ','.join(columns)
        self.cur = self.cnx.cursor()

    def close(self):
        self.cur.close()
        self.cnx.close()

    def insert_db(self, row):
        values = '","'.join(row)
        command = f'INSERT INTO {self.table}({self.keys}) VALUES("{values}")'

        self.cur.execute(command)
        self.cnx.commit()
        print(command)

    def show_table(self):
        comand = f'SELECT * FROM {self.table}'
        self.cur.execute(comand)
        result = self.cur.fetchall()
        return result

    def update_db(self, change, condition):
        command = f'UPDATE {self.table} SET {change} WHERE {condition}'
        self.cur.execute(command)
        self.cnx.commit()

    def delete_db(self, condition):
        command = f'DELETE FROM {self.table} WHERE {condition}'
        self.cur.execute(command)
        self.cnx.commit()
        print(command)

    def select_distinct(self, target, condition):
        comand = f'SELECT DISTINCT {target} FROM {self.table} {condition}'
        self.cur.execute(comand)
        result = self.cur.fetchall()
        return result

    def select_city(self,local):
        comand = f'SELECT * FROM {self.table}  WHERE local = "{local}"'
        self.cur.execute(comand)
        result = self.cur.fetchall()
        return result

    def select_table(self, condition):
        comand = f'SELECT * FROM {self.table} WHERE{condition}'
        self.cur.execute(comand)
        result = self.cur.fetchall()
        return result



def client_check(client_db, new_client):

    table = client_db.show_table()
    print(new_client)
    if new_client in table:
        print('cliente ja cadastrado')
        return False

    else:
        print('cadastrando cliente')
        return True



def create_table(table_name):
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='MrWh1t32',
        database='auctions_db'
    )
    cur = cnx.cursor()
    command = f"""CREATE TABLE if not exists  {table_name}(
    site VARCHAR(255),
    category varchar(255),
    price varchar(255),
    url varchar(255),
    city varchar(255)
    )"""
    cur.execute(command)
    cnx.commit()




auctions_db = Data_base_manager('auctions_db', 'auctions',
                                ['site','category', 'price', 'url', 'local'])

clientsDB = Data_base_manager('auctions_db', 'clients',
                              ['client_name', 'client_local'])



# print(len(auctions_db.show_table()))
# auctions_db.delete_db('site= "Zukerman"')
# print(len(auctions_db.show_table()))
