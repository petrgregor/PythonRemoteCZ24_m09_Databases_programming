# Add some grades for each student
from datetime import datetime

from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from models_students import *

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Grade(student=5, grade=1, date_created=datetime(2024, 10, 3, 12, 30)),
            Grade(student=5, grade=2, date_created=datetime(2024, 9, 3, 8, 30)),
            Grade(student=5, grade=1, date_created=datetime(2024, 9, 4, 9, 30)),
            Grade(student=6, grade=3, date_created=datetime(2024, 9, 3, 10, 30)),
            Grade(student=6, grade=2, date_created=datetime(2024, 10, 2, 12, 30)),
            Grade(student=6, grade=2, date_created=datetime(2024, 10, 2, 11, 30)),
            Grade(student=7, grade=1, date_created=datetime(2024, 10, 1, 13, 30)),
            Grade(student=7, grade=2, date_created=datetime(2024, 10, 2, 8, 30)),
            Grade(student=8, grade=2, date_created=datetime(2024, 10, 3, 10, 30)),
            Grade(student=8, grade=2, date_created=datetime(2024, 10, 1, 11, 30)),
            Grade(student=9, grade=3, date_created=datetime(2024, 10, 3, 8, 30)),
            Grade(student=10, grade=2, date_created=datetime(2024, 10, 3, 9, 30)),
            Grade(student=12, grade=2, date_created=datetime(2024, 10, 3, 12, 30)),
            Grade(student=13, grade=2, date_created=datetime(2024, 10, 3, 12, 30)),
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(f"ERROR: {e}")
