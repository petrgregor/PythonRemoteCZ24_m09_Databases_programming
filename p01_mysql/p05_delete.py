from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password, database="cinematic") as conn:
        with conn.cursor() as cursor:
            """Úkol 7
            Napište dotaz SQL, který odstraní tabulky z databáze cinematic. 
            Proveďte onen dotaz."""
            sql_statement = """DROP TABLE movies;"""
            cursor.execute(sql_statement)
            print("Tabulka 'movies' byla smazána.")
            sql_statement = """DROP TABLE directors;"""
            cursor.execute(sql_statement)
            print("Tabulka 'directors' byla smazána.")

except Error as e:
    print(e)

print("Konec")
