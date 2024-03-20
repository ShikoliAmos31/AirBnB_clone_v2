#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

class State(BaseModel, Base):
    """
    State class representation
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities_relation = relationship("City", cascade='all, delete, delete-orphan', backref="state")

    @property
    def cities(self):
        """
        Getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id
        """
        return [city for city in self.cities_relation]
