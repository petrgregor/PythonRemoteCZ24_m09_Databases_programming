from sqlalchemy_utils import database_exists, create_database

from connect_db import session, db
from models_cinematic import *

"""Úkol 1

Připojte se k serveru mysql a jako domovskou / výchozí databázi nastavte databázi cinematic. Vytvořte definici tabulky pomocí SQLAlchemy:

    Directors (třída) - tabulka directors: director_id (PK), name, surname, rating
    Movies (třída) - tabulka movies: movie_id (PK), title, year, category, director_id, rating
"""
if not database_exists(db.url):
    create_database(db.url)


"""Úkol 2

Přidání vztahů pro tabulku (director_id - FK):

    jeden režisér (director) -> mnoho filmů
    jeden film (movie) -> jeden režisér

Vytvořte tabulky v databázi."""
Base.metadata.create_all(db)
