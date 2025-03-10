#!/usr/bin/python3
"""Python - Object Relational Mapping"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """Base Class"""
    __tablename__ = "states"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
    cities = relationship("City", back_populates="state")
