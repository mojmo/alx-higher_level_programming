#!/usr/bin/python3

"""This script defines a SQLAlchemy model for the 'states' table."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A class representing a state for a MySQL database.

    Args:
    - __tablename__ (str): The name of the MySQL table that stores states.
    - id (sqlalchemy.Integer): The primary key of the state.
    - name (sqlalchemy.String): The name of the state.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
