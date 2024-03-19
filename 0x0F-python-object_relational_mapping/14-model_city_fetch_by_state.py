#!/usr/bin/python3
"""Get all the cityes in each state in the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
    ))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name, City.id, City.name).join(
        City).order_by(City.id)

    for row in result:
        print(f"{row[0]}: ({row[1]}) {row[2]}")
