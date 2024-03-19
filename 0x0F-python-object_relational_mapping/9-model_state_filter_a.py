#!/usr/bin/python3
"""Dipslay all states that has the letter 'a' in it"""

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

    states = session.query(State).filter(State.name.ilike('%a%')).order_by(
        State.id)

    for state in states.all():
        print(f"{state.id}: {state.name}")
