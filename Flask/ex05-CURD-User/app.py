from flask import Flask, render_template, request , make_response , jsonify
from flask_cors import CORS
import mysql.connector
import os , base64 , json
from dotenv import load_dotenv
import datetime
import time
load_dotenv()

app = Flask(__name__)
CORS(app)

mysql_host = os.getenv('DB_HOST')
mysql_user = os.getenv('DB_USER')
mysql_password = os.getenv('DB_PASSWORD')
mysql_database = os.getenv('DB_NAME')


@app.route('/api')
def read():
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=mysql_database)
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("""SELECT * FROM Users""")
    result = mycursor.fetchall()
    return result

if __name__ == '__main__':
    app.run(debug=True)