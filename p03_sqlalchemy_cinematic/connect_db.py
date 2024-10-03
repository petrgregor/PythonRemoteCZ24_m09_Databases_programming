from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from p01_mysql.connection_details import *

CONNECTION_STRING = "mysql+mysqlconnector://{user}:{password}@{host}/{database}"
db = create_engine(CONNECTION_STRING.format(user=user, password=password, host=host, database='cinematic2'))


"""Úkol 3

Vytvořte sezení (session), které budeme používat k provádění dotazů."""
Session = sessionmaker(bind=db)
session = Session()
