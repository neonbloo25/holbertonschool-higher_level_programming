#!/usr/bin/python3
'''
Write a script that lists all State objects from the database hbtn_0e_6_usa
'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Preparing our connection
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
        )

    # Creating our "Cursor"
    Session = sessionmaker(bind=engine)
    session = Session()

    #  Query
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    #  Finally close "cursor"
    session.close()
