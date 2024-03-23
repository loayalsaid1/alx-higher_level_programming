#!/usr/bin/python3
"""Get all the state in each city in the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
    ))
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City)
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
