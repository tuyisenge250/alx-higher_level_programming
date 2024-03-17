#!/usr/bin/python3
from sqlalchemy import create_engine
from model_state import Base,State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],sys.argv[2],sys.argv[3]))
    Base.metadata.create_all(engine)
    match = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")