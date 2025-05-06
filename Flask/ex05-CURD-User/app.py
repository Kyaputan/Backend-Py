from flask import Flask, render_template, request , make_response , jsonify
from flask_cors import CORS
import mysql.connector
import os , base64 , json
from dotenv import load_dotenv
import bcrypt 

load_dotenv()

app = Flask(__name__)
CORS(app)

mysql_host = os.getenv('DB_HOST')
mysql_user = os.getenv('DB_USER')
mysql_password = os.getenv('DB_PASSWORD')
mysql_database = os.getenv('DB_NAME')

@app.route('/')
def rander():
    try:
        mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=mysql_database)
        return "✅ Server is running!"
    except Exception as e:
        print("❌ Error creating table:", e)
        return "✅ Server is running!"


@app.route('/api' , methods=['GET'])
def read():
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=mysql_database)
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("""SELECT * FROM Users""")
    result = mycursor.fetchall()
    return result

@app.route('/register' , methods=['POST'])
def register():
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=mysql_database)
    mycursor = mydb.cursor(dictionary=True)
    data = request.get_json()
    Name = data['Name']
    Email = data['Email']
    Password = data['Password']
    hashed_password = bcrypt.hashpw(Password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    query = "INSERT INTO Users (Name , Email, Password) VALUES (%s ,%s, %s)"
    mycursor.execute(query, (Name ,Email, hashed_password))
    mydb.commit()
    return jsonify({"status": "success", "message": "User registered successfully"}), 200

@app.route('/login' , methods=['POST'])
def login():
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=mysql_database)
    mycursor = mydb.cursor(dictionary=True)
    data = request.get_json()
    Email = data['Email']
    query = "SELECT * FROM Users WHERE Email = %s"
    mycursor.execute(query, (Email,))
    result = mycursor.fetchone()
    if result:
        password = data['Password']
        hashed_password = result['Password']
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            return jsonify({"status": "success", "message": "Login successful"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid password"}), 401
    else:
        return jsonify({"status": "error", "message": "User not found"}), 404
    
@app.route('/delete' , methods=['POST'])
def delete():
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=mysql_database)
    mycursor = mydb.cursor(dictionary=True)
    data = request.get_json()
    Email = data['Email']
    query = "SELECT * FROM Users WHERE Email = %s"
    mycursor.execute(query, (Email,))
    result = mycursor.fetchone()
    if result:
        password = data['Password']
        hashed_password = result['Password']
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            query = "DELETE FROM Users WHERE Email = %s AND Password = %s"
            mycursor.execute(query, (Email, hashed_password))
            mydb.commit()
            return jsonify({"status": "success", "message": "User deleted successfully"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid password"}), 401
    else:
        return jsonify({"status": "error", "message": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)