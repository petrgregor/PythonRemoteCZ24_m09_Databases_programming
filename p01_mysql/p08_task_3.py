"""Úkol 3
Napište funkci insert_instruments, která bude zodpovědná za doplnění údajů do tabulky nástrojů.
Funkce by měla přijímat dva argumenty - připojení k databázi a seznam záznamů, které se mají vložit.
"""

from mysql.connector import connect, Error
from connection_details import *


def insert_instruments(connection, instruments_list):
    with connection.cursor() as cursor:
        sql_statement = """
            INSERT INTO instruments
            (name, family, difficulty)
            VALUES (%s, %s, %s);
        """
        cursor.executemany(sql_statement, instruments_list)
        connection.commit()


# Otestujte funkci na následujícím seznamu:
instruments = [
    ('guitar', 'strings', 'medium'),
    ('piano', 'keyboard', 'hard'),
    ('harp', 'strings', 'hard'),
    ('triangle', 'percussion', 'easy'),
    ('flute', 'woodwind', 'medium'),
    ('violin', 'string', 'medium'),
    ('tambourine', 'percussion', 'easy'),
    ('organ', 'keyboard', 'hard')
]

try:
    with connect(host=host, user=user, password=password, database='music') as conn:
        insert_instruments(conn, instruments)

except Error as e:
    print(e)
