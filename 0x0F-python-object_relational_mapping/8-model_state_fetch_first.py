#!/usr/bin/python3
from sqlalchemy import create_engine
from model_state import Base,State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ =="__main__":
    engine= create_engine('mysql+mysqldb://{}:{}@localhost:33096/{}'.format(sys.argv[1],sys.argv[2],sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    session = Session(bind=engine)
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=", ")