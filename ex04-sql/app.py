from flask import Flask, render_template, request , make_response , jsonify
from flask_cors import CORS
import mysql.connector
import os , base64 , json
from dotenv import load_dotenv
import datetime
load_dotenv()

app = Flask(__name__)
CORS(app)

# Load environment variables from .env file
mysql_host = os.getenv('DB_HOST')
mysql_user = os.getenv('DB_USER')
mysql_password = os.getenv('DB_PASSWORD')
db = 'test'

@app.route('/api')
def read():
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=db)
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select * FROM City;")
    result = mycursor.fetchall()
    return result

@app.route('/api/<int:id>')
def readid(id):
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = ("select * FROM City WHERE ID = %s")
    val = (id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)

@app.route('/api', methods=['POST'])
def create():
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=db)
    mycursor = mydb.cursor(dictionary=True)
    data = request.get_json()
    sql = "INSERT INTO City (NAME, Detail, Date) VALUES (%s, %s, %s)"
    val = (data['NAME'], data['Detail'], data['Date'])
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify(data), 201)
#     {
#   "NAME": "Rayong",
#   "Detail": "Rayong is a city ...",
#   "Date": "2025-04-14"
#      }

@app.route('/api/<int:id>', methods=['PUT'])
def update(id):
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=db)
    mycursor = mydb.cursor(dictionary=True)
    data = request.get_json()
    sql = "UPDATE City SET NAME = %s, Detail = %s, Date = %s WHERE ID = %s"
    val = (data['NAME'], data['Detail'], data['Date'], id)
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify(data), 200)

@app.route('/api/<int:id>', methods=['DELETE'])
def delete(id):
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "DELETE FROM City WHERE ID = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify({'message': 'deleted'}), 200)

if __name__ == '__main__':
    app.run(debug=True)