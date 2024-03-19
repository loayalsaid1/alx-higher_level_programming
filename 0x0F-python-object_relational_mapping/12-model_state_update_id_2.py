#!/usr/bin/python3
"""Update a record in the states table"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
    ))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).get(2)
    state.name = "New Mexico"
    session.add(state)
    session.commit()
