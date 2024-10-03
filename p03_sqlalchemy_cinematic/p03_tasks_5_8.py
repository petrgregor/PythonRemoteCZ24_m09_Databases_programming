from sqlalchemy import desc, and_, or_

from connect_db import session
from models_cinematic import *

"""Úkol 5

Vypište všechny filmy z kategorie Drama."""
print("Vypište všechny filmy z kategorie Drama.")
movies = session.query(Movie).filter(Movie.category == "Drama")
for movie in movies:
    print(movie)

"""Úkol 6

Vypište názvy filmů z kategorie Krimi, které byly natočeny po roce 1994. 
"""
print("-" * 80)
print("Vypište názvy filmů z kategorie Krimi, které byly natočeny po roce 1994.")
movies = session.query(Movie).filter(Movie.category == "Crime", Movie.year > 1994)
for movie in movies:
    print(movie)

"""Úkol 7

Vypište kategorie všech filmů a jejich rating u filmů, které byly natočeny v letech 2000-2010 
a jejichž rating je vyšší než 7, seřazené podle ratingu. """
print("-" * 80)
print("Vypište kategorie všech filmů a jejich rating u filmů, které byly natočeny v letech 2000-2010 "
      "a jejichž rating je vyšší než 7, seřazené podle ratingu.")
movies = session.query(Movie).filter(Movie.year >= 2000, Movie.year <= 2010, Movie.rating > 7).order_by(desc(Movie.rating))
for movie in movies:
    print(f"{movie.title} ({movie.category}) rating={movie.rating}")

"""Úkol 8

Vypište jména všech režisérů, jejichž rating je větší nebo rovno 6 
a jejichž křestní jméno začíná písmenem "D" nebo končí písmenem "n".
"""
print("-" * 80)
print("Vypište jména všech režisérů, jejichž rating je větší nebo rovno 6 "
      "a jejichž křestní jméno začíná písmenem 'D' nebo končí písmenem 'n'")
directors = session.query(Director).filter(and_(Director.rating >= 6, or_(Director.name.like("D%"), Director.name.like("%n"))))
for director in directors:
    print(director)
