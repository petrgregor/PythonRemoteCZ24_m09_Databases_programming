from connect_db import db
from sqlalchemy.sql import text

with db.connect() as conn:
    sql_statement = text("ALTER TABLE students ADD class_name VARCHAR(30)")
    conn.execute(sql_statement)
