"""Úkol 1

Připojte se k serveru mysql a jako domovskou / výchozí databázi nastavte databázi cinematic. Vytvořte definici tabulky pomocí SQLAlchemy:

    Directors (třída) - tabulka directors: director_id (PK), name, surname, rating
    Movies (třída) - tabulka movies: movie_id (PK), title, year, category, director_id, rating
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Director(Base):
    __tablename__ = "directors"
    director_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(30))
    surname = Column(String(30))
    rating = Column(Integer)

    def __repr__(self):
        return f"Director(name={self.name}, surname={self.surname}, rating={self.rating})"

    def __str__(self):
        return f"{self.name} {self.surname}"


class Movie(Base):
    __tablename__ = "movies"
    movie_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(50))
    year = Column(Integer)
    category = Column(String(30))
    director_id = Column(Integer, ForeignKey(Director.director_id), nullable=False)  # Úkol 2
    rating = Column(Integer)

    def __repr__(self):
        return f"Movie(title={self.title}, year={self.year}, category={self.category})"

    def __str__(self):
        return f"{self.title} ({self.year})"
