from dotenv import dotenv_values
import mysql.connector

passwd = dotenv_values(".env")["SQL_PASSWD"]

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="mysql",
    password=passwd)

in_code = input("Input country code: ").upper()
if len(in_code) != 2:
    print("Invalid country code")
    exit()

cur = cnx.cursor()
cur.execute("USE flight_game")
cur.execute(
    f"SELECT name, type FROM airport WHERE iso_country = \"{in_code}\" ORDER BY type desc"
)

row = cur.fetchone()
while row != None:
    print(f"{row[0]}, {row[1]}")
    row = cur.fetchone()

cnx.close()
