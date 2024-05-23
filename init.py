import mysql.connector
from dotenv import load_dotenv
import os
import sys

load_dotenv()

#Connect to mysql
print("Hello World I'm Ken 1")

# CREATE INITIAL TABLE 'randomNumberTable' in 'randomNumberDB'
cnx = mysql.connector.connect(
    user = 'root', 
    password = 'PQThai29112003', 
    host = 'localhost',
    database = 'randomNumberDB',
    port = '3306'
    )
cursor = cnx.cursor()
action1 = "CREATE TABLE randomNumberTable (randomNumber int);"
cursor.execute(action1)
cnx.commit()
cursor.close()
cnx.close()

# INSERT INITIAL NUMBER '0' IN 'randomNumberTable'
cnx = mysql.connector.connect(
    user = 'root', 
    password = 'PQThai29112003', 
    host = 'localhost',
    database = 'randomNumberDB',
    port = '3306'
    )
cursor = cnx.cursor()
action2 = "INSERT INTO randomNumberTable (randomNumber) VALUES (%s);"
cursor.execute(action2)
cnx.commit()
cursor.close()
cnx.close()
