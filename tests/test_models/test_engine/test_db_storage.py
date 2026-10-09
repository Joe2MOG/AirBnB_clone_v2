#!/usr/bin/python3
"""Tests for the DBStorage engine."""

import unittest
from os import getenv
from uuid import uuid4

import models
from models.city import City
from models.engine.db_storage import DBStorage
from models.state import State


@unittest.skipIf(
    getenv("HBNB_TYPE_STORAGE") != "db",
    "DBStorage tests require DB storage"
)
class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class."""

    def setUp(self):
        """Use the active DBStorage instance."""
        self.storage = models.storage
        self.created_objects = []

    def tearDown(self):
        """Delete objects created during each test."""
        for obj in reversed(self.created_objects):
            try:
                self.storage.delete(obj)
            except Exception:
                pass

        try:
            self.storage.save()
        except Exception:
            pass

    def test_instance_creation(self):
        """Test that storage is a DBStorage instance."""
        self.assertIsInstance(self.storage, DBStorage)

    def test_all_returns_dictionary(self):
        """Test that all returns a dictionary."""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_all_filters_state(self):
        """Test filtering by State class."""
        state = State(
            name="Test State {}".format(uuid4())
        )
        self.storage.new(state)
        self.storage.save()
        self.created_objects.append(state)

        result = self.storage.all(State)
        key = "State.{}".format(state.id)

        self.assertIn(key, result)
        self.assertIs(result[key], state)

    def test_all_filters_city(self):
        """Test filtering by City class."""
        state = State(
            name="Test State {}".format(uuid4())
        )
        self.storage.new(state)
        self.storage.save()
        self.created_objects.append(state)

        city = City(
            name="Test City {}".format(uuid4()),
            state_id=state.id
        )
        self.storage.new(city)
        self.storage.save()
        self.created_objects.append(city)

        result = self.storage.all(City)
        key = "City.{}".format(city.id)

        self.assertIn(key, result)
        self.assertIs(result[key], city)

    def test_new_and_save_object(self):
        """Test adding and saving an object."""
        state = State(
            name="New State {}".format(uuid4())
        )

        self.storage.new(state)
        self.storage.save()
        self.created_objects.append(state)

        key = "State.{}".format(state.id)
        result = self.storage.all(State)

        self.assertIn(key, result)

    def test_new_keeps_same_object(self):
        """Test that storage returns the same object instance."""
        state = State(
            name="Same Object {}".format(uuid4())
        )

        self.storage.new(state)
        self.storage.save()
        self.created_objects.append(state)

        key = "State.{}".format(state.id)
        result = self.storage.all(State)

        self.assertIs(result[key], state)

    def test_delete_object(self):
        """Test deleting a stored object."""
        state = State(
            name="Delete State {}".format(uuid4())
        )

        self.storage.new(state)
        self.storage.save()

        key = "State.{}".format(state.id)
        self.assertIn(key, self.storage.all(State))

        self.storage.delete(state)
        self.storage.save()

        self.assertNotIn(key, self.storage.all(State))

    def test_delete_none(self):
        """Test that deleting None does nothing."""
        result = self.storage.delete(None)
        self.assertIsNone(result)

    def test_save_returns_none(self):
        """Test that save returns None."""
        self.assertIsNone(self.storage.save())

    def test_reload_returns_none(self):
        """Test that reload initializes storage and returns None."""
        self.assertIsNone(self.storage.reload())
        self.assertIsInstance(self.storage.all(), dict)

    def test_close_returns_none(self):
        """Test that close removes the current session."""
        self.assertIsNone(self.storage.close())

        self.storage.reload()
        self.assertIsInstance(self.storage.all(), dict)


if __name__ == "__main__":
    unittest.main()
