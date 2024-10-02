""" Exercise 1
● Add an Address for each student
● Print out all students along with their addresses using a join()
"""
from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from models_students import *

# vytvoříme tabulku v databázi
Base.metadata.create_all(db)

# přidáme adresy k jednotlivým studentům
try:
    session.add_all(
        [
            Address(student=5, street_name="Hlavní", number=5, city="Brno"),
            Address(student=6, street_name="Jarní", number=7, city="Praha"),
            Address(student=7, street_name="Letní", number=12, city="Ostrava"),
            Address(student=8, street_name="Podzimní", number=1, city="Olomouc"),
            Address(student=9, street_name="Zimní", number=54, city="Jihlava"),
            Address(student=10, street_name="Náměstí Svobody", number=3, city="Znojmo"),
            Address(student=12, street_name="Malinovského náměstí", number=60, city="Brno"),
            Address(student=13, street_name="Nádražní", number=501, city="Praha"),
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(f"ERROR: {e}")

print("Všichni studenti a jejich adresy:")
rows = session.query(Student, Address).join(Address)
for student, address in rows:
    print(f"{student}: {address}")

print('-'*80)
print("Můžeme změnit pořadí tabulek ve výstupu")
rows1 = session.query(Address, Student).join(Address)
for address, student in rows1:
    print(f"{student}: {address}")

print('-'*80)
print("Všichni studenti z Brna")
#rows = session.query(Student, Address).join(Address).filter(Address.city == "Brno")
rows_Brno = rows.filter(Address.city == "Brno")  # nebo lze využít předchozí výsledek
for student, address in rows_Brno:
    print(f"{student}: {address}")

print('-'*80)
print("Všichni studenti z Brna uspořádaní abecedně podle příjmení")
#rows = session.query(Student, Address).join(Address).filter(Address.city == "Brno").order_by(Student.last_name)
rows_Brno_sorted = rows_Brno.order_by(Student.last_name)  # lze opět využít předchozí výsledek
for student, address in rows_Brno_sorted:
    print(f"{student}: {address}")

print('-'*80)
print("Změnit adresu Adama Bernaua na ulici 'Vedlejší'")
students = session.query(Student, Address).join(Address).filter(Student.first_name == "Adam", Student.last_name == "Bernau")
for student, address in students:
    print(f"{student}: {address}")
print('-'*40)
student, address = students[0]
print(f"{student}: {address}")
address.street_name = "Vedlejší"
session.commit()
print('-'*40)
student, address = students[0]
print(f"{student}: {address}")
