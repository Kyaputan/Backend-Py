from fastapi import FastAPI
from typing import Union
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()


mysql_host = os.getenv('DB_HOST')
mysql_user = os.getenv('DB_USER')
mysql_password = os.getenv('DB_PASSWORD')
mysql_database = os.getenv('DB_NAME')

app = FastAPI()

@app.get("/")
def read():
    try:
        mydb = mysql.connector.connect(host=mysql_host,user=mysql_user, password=mysql_password,db=mysql_database)
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM products")
        result = mycursor.fetchall()
        mycursor.close()
        mydb.close()

        return {"status": "success",
                "message": "✅ Server is running!",
                "data": result}
    except Exception as e:
        print("❌ Error connecting to database:", e)
        return {"status": "error",
                "message": "❌ Error connecting to database: " + str(e)}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)