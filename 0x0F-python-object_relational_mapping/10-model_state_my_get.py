#!/usr/bin/python3
"""Display the id of a state its name specefied by user"""

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

    result = session.query(State.id).filter_by(name=argv[4]).scalar()
    if result:
        print(result)
    else:
        print("Not found")
