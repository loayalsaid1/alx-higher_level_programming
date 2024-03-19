import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://loayalsaid1:Loay_alsaid04@localhost/{}'.format('hbtn_0e_6_usa'), pool_pre_ping=True)
    Base.metadata.create_all(engine)
