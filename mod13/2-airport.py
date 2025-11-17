from dotenv import dotenv_values
import mysql.connector
from flask import Flask

passwd = dotenv_values(".env")["SQL_PASSWD"]

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="mysql",
    password=passwd)
cur = cnx.cursor()
cur.execute("USE flight_game")

app = Flask(__name__)

@app.route("/airport/<in_icao>")
def airportFromIcao(in_icao):
    cur.execute(
        f"SELECT name, municipality FROM airport WHERE ident = \"{in_icao}\""
    )
    row = cur.fetchone()
    if row != None:
        return obj(in_icao, row[0], row[1])
    else:
        return "Error", 404

def obj(icao, nam, mun) -> dict:
    return {
        "ICAO": icao,
        "Name": nam,
        "Location": mun,
    }
