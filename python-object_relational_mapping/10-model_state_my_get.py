#!/usr/bin/python3
"""
Write a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':

    # Collect data from argv arguments
    username = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_name = argv[4]

    # Make connection
    engine = create_engine(
        f'mysql+mysqldb://{username}:{passwd}@localhost:3306/{db}'
        )

    # Make 'cursor'
    session = sessionmaker(bind=engine)
    session = session()

    # Fetch only first row
    states = session.query(State).filter(State.name == state_name).all()
    if states:
        [print(f"{state.id}") for state in states]
    else:
        print("Not found")

    session.close()
