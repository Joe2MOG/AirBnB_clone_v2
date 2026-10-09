#!/usr/bin/python3
"""Defines the Place class."""

from os import getenv

from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    Table
)
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """Represent a place."""

    __tablename__ = "places"

    city_id = Column(
        String(60),
        ForeignKey("cities.id"),
        nullable=False
    )

    user_id = Column(
        String(60),
        ForeignKey("users.id"),
        nullable=False
    )

    name = Column(
        String(128),
        nullable=False
    )

    description = Column(
        String(1024),
        nullable=True
    )

    number_rooms = Column(
        Integer,
        nullable=False,
        default=0
    )

    number_bathrooms = Column(
        Integer,
        nullable=False,
        default=0
    )

    max_guest = Column(
        Integer,
        nullable=False,
        default=0
    )

    price_by_night = Column(
        Integer,
        nullable=False,
        default=0
    )

    latitude = Column(
        Float,
        nullable=True
    )

    longitude = Column(
        Float,
        nullable=True
    )

    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
            overlaps="place_amenities"
        )

        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
            back_populates="place_amenities"
        )

    else:
        amenity_ids = []

        @property
        def reviews(self):
            """Return Review instances linked to this Place."""
            from models import storage
            from models.review import Review

            return [
                review
                for review in storage.all(Review).values()
                if review.place_id == self.id
            ]

        @property
        def amenities(self):
            """Return Amenity instances linked to this Place."""
            from models import storage
            from models.amenity import Amenity

            amenities = []

            for amenity_id in self.amenity_ids:
                key = "Amenity.{}".format(amenity_id)
                amenity = storage.all(Amenity).get(key)

                if amenity is not None:
                    amenities.append(amenity)

            return amenities

        @amenities.setter
        def amenities(self, obj):
            """Add an Amenity id to this Place."""
            from models.amenity import Amenity

            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
