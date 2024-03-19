#!/usr/bin/python3
"""Insert a new object to the database
    Display the new object ID after being added to the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
    ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    print(state.id)
