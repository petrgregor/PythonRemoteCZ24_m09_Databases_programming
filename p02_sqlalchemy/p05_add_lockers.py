from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from models_students import *

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Locker(number=1, student=5),
            Locker(number=2, student=8),
            Locker(number=3, student=9),
            Locker(number=4, student=7),
            Locker(number=5, student=10)
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(f"ERROR: {e}")
