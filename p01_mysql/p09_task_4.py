"""Úkol 4

Napište funkci get_instruments_count, která zobrazí počet nástrojů pro každou kategorii.
Funkce by měla jako argument přijmout spojení.
Vrátí záznamy tvořené slovníky se dvěma klíči - 'family' a 'count'.
"""

from mysql.connector import connect, Error
from connection_details import *


def get_instruments_count(connection):
    with connection.cursor(dictionary=True) as cursor:
        sql_statement = """
            SELECT family, count(*) as count
            FROM instruments
            GROUP BY family;
        """
        cursor.execute(sql_statement)
        return cursor.fetchall()


try:
    with connect(host=host, user=user, password=password, database='music') as conn:
        result = get_instruments_count(conn)
        for instrument in result:
            print(instrument)

except Error as e:
    print(e)
