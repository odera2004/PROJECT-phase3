from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine =  create_engine("sqlite:///Business_management.db")


# create a session
Session =  sessionmaker(bind=engine)
session = Session()