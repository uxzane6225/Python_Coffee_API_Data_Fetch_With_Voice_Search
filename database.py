import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

db_host= os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_db = os.getenv("DB_DB")


try:
    cnx = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_db)
except mysql.connector.Error as err:
    if err.errno == mysql.connector.ER_ACCESS_DENIED_ERROR:
        print("Username and Password Invalid")
    elif err.errno == mysql.connector.ER_BAD_DB_ERROR:
        print("Databose doesn't exist")
    else:
        print(f"DB ERROR: {err}")
