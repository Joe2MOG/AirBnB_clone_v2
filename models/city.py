#!/usr/bin/python3
"""Defines the City class."""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """Represent a city."""

    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(
        String(60),
        ForeignKey("states.id"),
        nullable=False
    )

    places = relationship(
        "Place",
        backref="cities",
        cascade="all, delete, delete-orphan"
    )
