#!/usr/bin/python3

"""
Script to update the name of a State object with a specific ID
in a MySQL database.

Usage: ./script_name.py mysql_username mysql_password database_name
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a connection to the MySQL database using the provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create the database schema
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
