from mysql.connector import connect, Error
from connection_details import *


try:
    with connect(host=host, user=user, password=password, database="cinematic") as conn:
        with conn.cursor() as cursor:
            sql_statement = """SELECT * FROM movies;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            print("============== MOVIES =================")
            print("id\ttitle\tyear\tcategory\tdirector_id\trating")
            for movie in movies:
                print(f"{movie[0]}\t{movie[1]}\t{movie[2]}\t{movie[3]}\t{movie[4]}\t{movie[5]}")

            sql_statement = """SELECT * FROM directors;"""
            cursor.execute(sql_statement)
            directors = cursor.fetchall()
            print("============== DIRECTORS =================")
            for director in directors:
                print(director)

            task = """Úkol 6
Napište dotaz SQL, který vrátí všechny filmy z roku 2002. Proveďte onen dotaz."""
            print("============== MOVIES (year = 2002) =================")
            sql_statement = """SELECT * FROM movies WHERE year = 2002;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            for movie in movies:
                print(movie)

            print("============== MOVIES (year = 1994) =================")
            sql_statement = """SELECT * FROM movies WHERE year = 1994;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            for movie in movies:
                print(movie)

except Error as e:
    print(e)

print("Konec")
