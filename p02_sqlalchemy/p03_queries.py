from connect_db import session, db
from models_students import Student
from sqlalchemy.sql import text

with db.connect() as conn:
    sql_statement = text("SELECT * FROM students")
    rows = conn.execute(sql_statement)
    for row in rows:
        print(row)

print('-'*80)
print("Všichni studenti v databázi:")
# SELECT * FROM students;
students = session.query(Student).all()  # vrací seznam objektů
print(f"students: {students}")
for student in students:
    print(student)

print('-'*80)
print("Počet studentů v databázi:")
total = session.query(Student).count()
print(f"Počet: {total}")

print('-'*80)
print("Studenti s id >= 8")
"""
SELECT * FROM students
WHERE students.id >= 8
"""
rows = session.query(Student).filter(Student.id >= 8)
print(rows)
for row in rows:
    print(row)
