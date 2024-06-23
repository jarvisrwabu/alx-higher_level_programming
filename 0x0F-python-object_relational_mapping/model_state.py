#!/usr/bin/python3
"""Class Definition of state table."""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    Base = declarative_base()

    class State(Base):
        """Class definition of a state db."""

        __tablename__ = 'states'
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
