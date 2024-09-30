from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            sql_statement = "SHOW DATABASES"
            cursor.execute(sql_statement)
            databases = cursor.fetchall()
            for database in databases:
                print(database[0])

except Error as e:
    print(e)

print("-"*80)
print("Konec")
