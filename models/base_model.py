#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime

import models
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """Base class for all AirBnB objects."""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        for key, value in kwargs.items():
            if key == "__class__":
                continue

            if (
                key in ("created_at", "updated_at")
                and isinstance(value, str)
            ):
                value = datetime.fromisoformat(value)

            setattr(self, key, value)

        if "id" not in kwargs:
            self.id = str(uuid.uuid4())

        if "created_at" not in kwargs:
            self.created_at = datetime.now()

        if "updated_at" not in kwargs:
            self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict.pop("_sa_instance_state", None)

        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            obj_dict
        )

    def save(self):
        """Update updated_at and save the object."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()

        if "_sa_instance_state" in result:
            del result["_sa_instance_state"]

        return result

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)
