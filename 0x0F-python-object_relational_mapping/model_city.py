#!/usr/bin/python3
"""Model city"""
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """A city model"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship('State', backref='cities')
