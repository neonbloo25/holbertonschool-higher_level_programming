#!/usr/bin/python3
"""Python - Object Relational Mapping"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """Base Class"""
    __tablename__ = "cities"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
