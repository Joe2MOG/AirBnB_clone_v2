#!/usr/bin/python3
"""Defines the DBStorage engine."""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Manage storage of AirBnB models in a MySQL database."""

    __engine = None
    __session = None

    def __init__(self):
        """Create the SQLAlchemy engine."""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        url = "mysql+mysqldb://{}:{}@{}/{}".format(
            user,
            password,
            host,
            database
        )

        self.__engine = create_engine(
            url,
            pool_pre_ping=True
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return database objects as a dictionary."""
        classes = {
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        objects = {}

        if cls is not None:
            if isinstance(cls, str):
                cls = classes.get(cls)

            if cls is None:
                return objects

            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(
                    obj.__class__.__name__,
                    obj.id
                )
                objects[key] = obj

            return objects

        for model_class in classes.values():
            for obj in self.__session.query(model_class).all():
                key = "{}.{}".format(
                    obj.__class__.__name__,
                    obj.id
                )
                objects[key] = obj

        return objects

    def new(self, obj):
        """Add an object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit changes in the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create database tables and initialize the session."""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )

        self.__session = scoped_session(session_factory)

    def close(self):
        """Remove the current scoped session."""
        self.__session.remove()
