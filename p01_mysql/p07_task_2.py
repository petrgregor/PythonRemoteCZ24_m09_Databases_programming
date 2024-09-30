from mysql.connector import connect, Error
from connection_details import *


"""Úkol 2
Napište skript, který vytvoří databázi music s tabulkou:

nástroje: instrument_id(PK, autoincrement), name, family, difficulty(enum - easy, medium, hard)
"""
try:
    with connect(host=host, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            sql_statement = "CREATE DATABASE IF NOT EXISTS music"
            cursor.execute(sql_statement)
            print("Databáze 'music' byla vytvořena.")

            sql_statement = """
                CREATE TABLE IF NOT EXISTS music.instruments (
                    instrument_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                    name VARCHAR(30) NOT NULL,
                    family VARCHAR(30) NOT NULL,
                    difficulty ENUM('easy', 'medium', 'hard') NOT NULL 
                )
            """
            cursor.execute(sql_statement)
            print("Tabulka 'instruments' byla vytvořena.")

except Error as e:
    print(e)

print("-"*80)
print("Konec")
