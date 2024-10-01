from sqlalchemy_utils import database_exists, create_database

from connect_db import db
from models_students import Base

print(f"db.url = {db.url}")

if not database_exists(db.url):
    create_database(db.url)

Base.metadata.create_all(db)  # vytvoří tabulky z tříd definovaných v models_students.py
