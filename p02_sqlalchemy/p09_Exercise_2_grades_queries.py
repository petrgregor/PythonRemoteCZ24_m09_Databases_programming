from sqlalchemy import func, delete

from connect_db import session
from models_students import *

print("Všechny známky - výpis ve formátu: jméno a příjmení studenta: známka")
rows = session.query(Student, Grade).join(Grade)
for student, grade in rows:
    print(f"{student.first_name} {student.last_name}: {grade.grade}")

print("-" * 80)
print("Výpis všech známek pro každého studenta")
students = session.query(Student).order_by(Student.last_name)
for student in students:
    print(f"{student.last_name} {student.first_name}:")
    grades = session.query(Grade).filter(Grade.student == student.id)
    for grade in grades:
        print(f"\t{grade.grade} ({grade.date_created})")
    if grades.count() == 0:
        print("\tNehodnocen(a)")

print("-" * 80)
print("Výpis počtu známek pro každého studenta")
for student in students:
    grades = session.query(Grade).filter(Grade.student == student.id).count()
    print(f"{student.last_name} {student.first_name}: má {grades} známek")
print("-" * 40)
# pomocí agregační funkce
rows = session.query(Student, func.count(Grade.id)).join(Grade).group_by(Student.id).order_by(Student.last_name)
for student, grades in rows:
    print(f"{student.last_name} {student.first_name}: má {grades} známek")

print("-" * 80)
print("Výpis průměrné známky pro každého studenta")
averages = session.query(Student, func.avg(Grade.grade)).join(Grade).group_by(Student.id).order_by(Student.last_name)
for student, average in averages:
    print(f"{student.last_name} {student.first_name} má průměrné hodnocení {average}")

print("-" * 80)
print("Student s nejlepším průměrným hodnocením")
best_student, average = min(averages, key=lambda x: x[1])
print(f"Nejlepší student je {best_student.first_name} {best_student.last_name} s průměrným hodnocením {average}.")

print("-" * 80)
print("Smazání nejstarší známky")
oldest_grade = session.query(Grade).order_by(Grade.date_created).first()
session.delete(oldest_grade)
session.commit()
