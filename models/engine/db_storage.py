#!/usr/bin/python3
"""Temporary DBStorage interface for the AirBnB project."""


class DBStorage:
    """Provide the storage interface required by the project."""

    def __init__(self):
        """Initialize temporary in-memory storage."""
        self.__objects = {}

    def all(self, cls=None):
        """Return all objects, optionally filtered by class."""
        if cls is None:
            return self.__objects

        return {
            key: obj
            for key, obj in self.__objects.items()
            if isinstance(obj, cls)
        }

    def new(self, obj):
        """Add an object to temporary storage."""
        key = "{}.{}".format(
            obj.__class__.__name__,
            obj.id
        )
        self.__objects[key] = obj

    def save(self):
        """Placeholder for database transaction commit."""
        pass

    def delete(self, obj=None):
        """Delete an object from temporary storage."""
        if obj is None:
            return

        key = "{}.{}".format(
            obj.__class__.__name__,
            obj.id
        )

        if key in self.__objects:
            del self.__objects[key]

    def reload(self):
        """Placeholder for database session initialization."""
        pass

    def close(self):
        """Placeholder for closing a database session."""
        pass
