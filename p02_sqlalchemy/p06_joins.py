from connect_db import session
from models_students import Student, Locker

print("Spojíme studenty se skříňkami, studenti, kteří mají skříňku:")
rows = session.query(Student).join(Locker)
print(rows)
for row in rows:
    print(row)

print('-'*80)
rows = session.query(Student, Locker).join(Locker)
print(rows)
for row in rows:
    print(row)
print('-'*40)
for row in rows:
    student, locker = row
    print(f"{locker}: {student}")

print('-'*80)
print("Student se skříňkou #4")
rows = session.query(Student).join(Locker).filter(Locker.number == 4)
for row in rows:
    print(row)

print('-'*80)
print("Uspořádáme podle čísla skříňky")
rows = session.query(Student, Locker).join(Locker).order_by(Locker.number)
print(rows)
for row in rows:
    print(row)
    print(f"Skříňka #{row[1].number} patří studentovi {row[0]}")
print('-'*40)
for student, locker in rows:
    print(f"{locker}: {student}")
