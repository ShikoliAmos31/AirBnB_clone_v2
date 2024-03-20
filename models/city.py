#!/usr/bin/python3
"""This module contains the City class."""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from models.place import Place  # Add this import statement

class City(BaseModel, Base):
    """City class that inherits from BaseModel."""

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")

    def __init__(self, *args, **kwargs):
        """Initialize City class."""
        super().__init__(*args, **kwargs)
