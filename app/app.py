import mysql.connector
from flask import Flask
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
#run app:
#python3 -m flask run
#Define root route
@app.route('/')
def hello_world():
    return 'Hello World !'

# Database configuration
db_host = os.environ.get("DATABASE_HOST")
db_user = os.environ.get("DATABASE_USER")
db_password = os.environ.get("DATABASE_PASSWORD")
db_name = os.environ.get("DATABASE_NAME")

#Get list of products
@app.route('/products')
def get_products():
    database = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = database.cursor()
    cursor.execute("SELECT * FROM tblProduct")
    row_headers=[x[0] for x in cursor.description]
    products = cursor.fetchall()
    json_data=[]
    for product in products:
        json_data.append(dict(zip(row_headers,product)))
    cursor.close()
    return json.dumps(json_data) #convert to JSON

#use this function to create Database 
@app.route('/initdb')
def initdb():
    database = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password      
    )
    cursor = database.cursor()
    cursor.execute("DROP DATABASE IF EXISTS ProductManagement")
    cursor.execute("CREATE DATABASE ProductManagement")
    cursor.close()    
    return 'init Database' #Good     
#write a function to create tables
@app.route('/init_tables')
def init_tables():
    database = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = database.cursor()

    cursor.execute("DROP TABLE IF EXISTS tblProduct")
    cursor.execute("""CREATE TABLE tblProduct """
    """(id INT PRIMARY KEY AUTO_INCREMENT,"""
    """name VARCHAR(255),""" 
    """description VARCHAR(255))""")
    cursor.close()    
    return "init_tables"

