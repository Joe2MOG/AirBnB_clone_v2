#!/usr/bin/python3
"""Tests for the FileStorage engine."""

import unittest
from os import getenv

from models import storage
from models.base_model import BaseModel
from models.city import City
from models.state import State


@unittest.skipIf(
    getenv("HBNB_TYPE_STORAGE") == "db",
    "FileStorage tests require FileStorage"
)
class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def test_all(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Test adding an object to storage."""
        model = BaseModel()

        storage.new(model)

        key = "BaseModel.{}".format(model.id)

        self.assertIn(key, storage.all())
        self.assertIs(storage.all()[key], model)

        storage.delete(model)

    def test_save_reload(self):
        """Test saving and reloading an object."""
        model = BaseModel()

        storage.new(model)
        storage.save()

        key = "BaseModel.{}".format(model.id)

        storage.reload()

        self.assertIn(key, storage.all())

        storage.delete(storage.all()[key])
        storage.save()

    def test_all_with_class(self):
        """Test filtering stored objects by class."""
        state = State()
        city = City()

        storage.new(state)
        storage.new(city)

        states = storage.all(State)

        state_key = "State.{}".format(state.id)
        city_key = "City.{}".format(city.id)

        self.assertIn(state_key, states)
        self.assertNotIn(city_key, states)

        storage.delete(state)
        storage.delete(city)

    def test_delete(self):
        """Test deleting an object from storage."""
        model = BaseModel()

        storage.new(model)

        key = "BaseModel.{}".format(model.id)

        self.assertIn(key, storage.all())

        storage.delete(model)

        self.assertNotIn(key, storage.all())

    def test_delete_none(self):
        """Test that deleting None does nothing."""
        before = len(storage.all())

        storage.delete(None)

        after = len(storage.all())

        self.assertEqual(before, after)

    def test_all_without_class(self):
        """Test that all without a class returns all objects."""
        state = State()
        city = City()

        storage.new(state)
        storage.new(city)

        objects = storage.all()

        state_key = "State.{}".format(state.id)
        city_key = "City.{}".format(city.id)

        self.assertIn(state_key, objects)
        self.assertIn(city_key, objects)

        storage.delete(state)
        storage.delete(city)


if __name__ == "__main__":
    unittest.main()
