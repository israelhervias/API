
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, send_file, request
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import json

user = "ihhmoney"
passw = "loco123123"
host = "ihhmoney.mysql.pythonanywhere-services.com"
database = "ihhmoney$foodb"

app = Flask(__name__)

def connect():
    db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
    conn = db.connect()
    return conn

def disconnect(conn):
    conn.close()

@app.route('/')
def home(methods = ["GET"]):
    #img_path = "/home/automato/website/img/home.gif"
    return("Python anywhre")

@app.route('/api/v1/tables', methods = ["GET"])
def show_tables():
    conn = connect()
    tables = conn.execute(
        "SHOW TABLES;"
    )
    tables_dict = {}
    tables_lst = [table[0] for table in tables.fetchall()]
    tables_dict["tables"] = tables_lst
    tables_json = json.dumps(tables_dict)
    #print(tables_json)
    disconnect(conn)
    return tables_json

@app.route('/api/v1/food/names', methods = ["GET"])
def show_food_names():
    if "rows" in request.args:
        rows = int(request.args["rows"])
    else:
        rows = None
    conn = connect()
    sql = "SELECT name FROM food"
    if rows:
        sql = sql + " LIMIT {0}".format(rows)
    else:
        sql = sql + ";"
    food_names = conn.execute(
        "SELECT name FROM food;"
    )
    food_names_dict = {}
    food_names_lst = [food_name[0] for food_name in food_names.fetchall()]
    food_names_dict["food names"] = food_names_lst
    food_names_dict["number of rows"] = len(food_names_lst)
    food_names_json = json.dumps(food_names_dict)
    #print(food_names_json)
    disconnect(conn)
    return food_names_json


@app.route('/api/v1/food/<string:name>', methods = ["GET"])
def search_food_by_name():

    conn = connect()
    sql = """
        SELECT *
        FROM food
        WHERE UPPER(name) = UPPER('{0}')
        """.format(name)

    food = conn.execute(sql)
    food_dict = {}
    food_lst = [list(food.fetchone())]
    food_dict["food"] = food_lst
    food_json = json.dumps(food_dict)
    #print(food_names_json)
    disconnect(conn)
    return food_json


