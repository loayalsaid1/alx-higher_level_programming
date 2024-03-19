#!/usr/bin/python3
"""Delete states with letter 'a' in the name from the database"""
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

    session.query(State).filter(State.name.ilike('%a%')).delete(
        synchronize_session='fetch')
    session.commit()
