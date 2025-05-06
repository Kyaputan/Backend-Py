from flask import Flask, request , make_response , jsonify
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv
import time
load_dotenv()

app = Flask(__name__)
CORS(app)


mysql_host = os.getenv('DB_HOST')
mysql_user = os.getenv('DB_USER')
mysql_password = os.getenv('DB_PASSWORD')
db = 'My_DB'



@app.route('/api')
def read():
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=db)
    time.sleep(0.2)
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM Customers")
    result = mycursor.fetchall()
    return result

@app.route('/api/<int:id>')
def readid(id):
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = ("select * FROM Customers WHERE CustomerID = %s")
    val = (id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)

@app.route('/api/<city>')
def readcity(city):
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = ("select * FROM Customers WHERE City = %s")
    val = (city,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return make_response(jsonify(result), 200)

@app.route('/api', methods=['POST'])
def create():
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=db)
    mycursor = mydb.cursor(dictionary=True)
    data = request.get_json()
    sql = 'INSERT INTO Customers (Name, Address, City , PostalCode) VALUES (%s, %s, %s, %s)'
    val = (data['Name'], data['Address'], data['City'], data['PostalCode'])
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify(data), 201)

# {
#     "Name": "Rachata Singkhet",
#     "Address": "94/4 Rayong",
#     "City": "Rayong",
#     "PostalCode": "21000"
# }

@app.route('/api/<int:id>', methods=['PUT'])
def update(id):
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=db)
    mycursor = mydb.cursor(dictionary=True)
    data = request.get_json()
    sql = "UPDATE Customers SET Name = %s, Address = %s, City = %s ,PostalCode =%s WHERE CustomerID = %s"
    val = (data['Name'], data['Address'], data['City'], data['PostalCode'], id)
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify(data), 200)

@app.route('/api/<int:id>', methods=['DELETE'])
def delete(id):
    mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=db)
    mycursor = mydb.cursor(dictionary=True)
    sql = "DELETE FROM Customers WHERE CustomerID = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify({'message': 'deleted'}), 200)

if __name__ == '__main__':
    app.run(debug=True)
    

# SELECT * FROM Customers 
# JOIN Pets ON Customers.CustomerID = Pets.CustomerID 
# WHERE Customers.City = 'Bangkok' AND (Pets.PetType ='Dog' OR Pets.PetType = 'Cat');



# SELECT p.CustomerID , u.Name ,SUM(p.Price) as PriceSUM
# FROM Pets p
# LEFT JOIN Customers u ON p.CustomerID = u.CustomerID
# GROUP BY p.CustomerID, u.Name
# LIMIT 0, 25;