#!/usr/bin/python3
"""Class Definition of state table."""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

if __name__ == "__main__":
    Base = declarative_base()

    class State(Base):
        """Class definition of a state db."""

        __tablename__ = 'states'
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)
