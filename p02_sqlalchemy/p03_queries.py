from sqlalchemy import and_, or_, desc

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

print('-'*80)
print("Studenti, jejichž příjemní začíná na 'Svob'")
rows = session.query(Student).filter(Student.last_name.like("Svob%"))
for row in rows:
    print(row)

print('-'*80)
print("Studenti s id > 8 a příjmení začínající na 'Čer'")
rows = session.query(Student).filter(Student.id > 8, Student.last_name.like("Čer%"))
#rows = session.query(Student).filter(and_(Student.id > 8, Student.last_name.like("Čer%")))
for row in rows:
    print(row)

print('-'*80)
print("Studenti, jejichž jméno NEBO příjmení začíná na 'B'")
rows = session.query(Student).filter(or_(Student.first_name.like('B%'), Student.last_name.like('B%')))
#session.add(Student(first_name="Gusta", last_name="Beneš"))
#session.commit()
for row in rows:
    print(row)
print('-'*40)
#session.add(Student(first_name="Helena", last_name="Budínská"))
#session.commit()
for row in rows:
    print(row)

print('-'*80)
print("Všichni studenti uspořádaní podle příjmení.")
rows = session.query(Student).order_by(Student.last_name, Student.first_name)
for row in rows:
    print(row)

print('-'*80)
print("Všichni studenti uspořádaní podle příjmení sestupně.")
rows = session.query(Student).order_by(desc(Student.last_name), desc(Student.first_name))
for row in rows:
    print(row)

print('-'*80)
print("Studenti s id >= 8 uspořádaní abecedně podle příjmení:")
rows = session.query(Student).filter(Student.id >= 8).order_by(Student.last_name)
for row in rows:
    print(row)

print('-'*80)
print("Offset = 3 (přeskočí první tři záznamy)")
rows = session.query(Student).offset(3)
for row in rows:
    print(row)

print('-'*80)
print("Studenti s id >= 8, vynechat první 2 řádky")
rows = session.query(Student).filter(Student.id >= 8).offset(2)
for row in rows:
    print(row)

print('-'*80)
print("První tři studenti příjmení dle abecedy")
rows = session.query(Student).order_by(Student.last_name).limit(3)
for row in rows:
    print(row)

print('-'*80)
print("První student")
rows = session.query(Student).limit(1)  # seznam (list), který obsahuje jednoho studenta
for row in rows:
    print(row)
print('-'*40)
print(rows[0])
print('-'*40)
result = session.query(Student).first()  # jeden student (jeden objekt)
#for row in rows:
#    print(row)
# TypeError: 'Student' object is not iterable
print(result)

print('-'*80)
print("Student s id == 8")
rows = session.query(Student).filter(Student.id == 8)  # seznam obsahující jednoho studenta
for row in rows:
    print(row)
print('-'*40)
# LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
#   result = session.query(Student).get(8)
result = session.query(Student).get(8)  # jeden objekt
print(result)
