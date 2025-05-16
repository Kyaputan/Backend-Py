from fastapi import FastAPI , Depends
from mysql.connector import pooling
from mysql.connector.connection import MySQLConnection
from typing import Generator
import os
from dotenv import load_dotenv
load_dotenv()

mysql_host = os.getenv('DB_HOST')
mysql_user = os.getenv('DB_USER')
mysql_password = os.getenv('DB_PASSWORD')
mysql_database = os.getenv('DB_NAME')

dbconfig = {
    "host": mysql_host,
    "user": mysql_user,
    "password": mysql_password,
    "database": mysql_database
}

connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    **dbconfig
)


def get_db() -> Generator[MySQLConnection, None, None]:
    db = connection_pool.get_connection()
    try:
        yield db
    finally:
        db.close()



app = FastAPI()

@app.get("/")
def read(db: MySQLConnection = Depends(get_db)):
    try:
        mycursor = db.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM products")
        result = mycursor.fetchall()
        mycursor.close()
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