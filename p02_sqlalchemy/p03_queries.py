from connect_db import session
from models_students import Student

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
