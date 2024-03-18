import mysql.connector

conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="nandhu07122003",
        database = "coustomerdata"
)

mycur=conn.cursor()
query="drop table student;"
mycur.execute(query)

