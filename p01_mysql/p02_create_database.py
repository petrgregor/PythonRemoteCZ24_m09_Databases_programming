from mysql.connector import connect, Error
from connection_details import *

try:
    """Úkol 1
    Z Pythonu se připojte k serveru mysql. Poté vytvořte databázi cinematic."""
    with connect(host=host, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE cinematic;")
        print("Databáze 'cinematic' byla vytvořena.")


except Error as e:
    print(e)

"""Úkol 2
Připojte se k serveru mysql nastavením databáze cinematic jako domovské / výchozí databáze."""
try:
    with connect(host=host, user=user, password=password, database="cinematic") as conn:
        print(conn)

except Error as e:
    print(e)

"""Úkol 3
Napište dotaz SQL, který v databázi cinematic vytvoří následující tabulky:

directors (režiséři): director_id(PK), name, surname, rating
movies (filmy): movie_id(PK), title, year, category, director_id(FK), rating
"""
try:
    with connect(host=host, user=user, password=password, database="cinematic") as conn:
        create_table_directors = """
            CREATE TABLE IF NOT EXISTS directors (
                director_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                name VARCHAR(30),
                surname VARCHAR(30) NOT NULL,
                rating INT
            ) DEFAULT CHARACTER SET utf8;
        """
        create_table_movies = """
            CREATE TABLE IF NOT EXISTS movies (
                movie_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                title VARCHAR(50),
                year SMALLINT,
                category VARCHAR(30),
                director_id INT NOT NULL,
                rating INT,
                CONSTRAINT `movies_director` FOREIGN KEY (`director_id`) REFERENCES `directors` (director_id)
            ) DEFAULT CHARACTER SET utf8;
        """

        """Úkol 4
        Spusťte dotaz, který jste napsali dříve, a vytvořte tabulky v databázi cinematic."""
        with conn.cursor() as cursor:
            cursor.execute(create_table_directors)
            print("Tabulka 'directors' byla vytvořena.")
            cursor.execute(create_table_movies)
            print("Tabulka 'movies' byla vytvořena.")


except Error as e:
    print(e)

print("Konec")
