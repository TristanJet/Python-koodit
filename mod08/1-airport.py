from dotenv import dotenv_values
import mysql.connector

passwd = dotenv_values(".env")["SQL_PASSWD"]

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="mysql",
    password=passwd)

in_icao = input("Input ICAO: ").upper()

cur = cnx.cursor()
cur.execute("USE flight_game")
cur.execute(
    f"SELECT name, municipality FROM airport WHERE ident = \"{in_icao}\""
)

row = cur.fetchone()
if row != None:
    print(f"{row[0]}, {row[1]}")
else:
    print(f"ICAO: {in_icao} was not found in database")

cnx.close()
