#!/usr/bin/python3
"""Defines the State class."""

from os import getenv

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class State(BaseModel, Base):
    """Represent a state."""

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete, delete-orphan"
        )
    else:
        @property
        def cities(self):
            """Return City instances linked to this State."""
            from models import storage
            from models.city import City

            return [
                city
                for city in storage.all(City).values()
                if city.state_id == self.id
            ]
