#!/usr/bin/python3
"""Tests for the FileStorage class."""

import unittest
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.state import State


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def test_all(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Test adding an object to storage."""
        model = BaseModel()
        storage.new(model)

        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, storage.all())
        self.assertIs(storage.all()[key], model)

    def test_save_reload(self):
        """Test saving and reloading an object."""
        model = BaseModel()
        model.name = "Test"
        storage.new(model)
        storage.save()

        storage.reload()

        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, storage.all())

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

    def test_delete(self):
        """Test deleting an object from storage."""
        model = BaseModel()
        storage.new(model)

        key = "{}.{}".format(model.__class__.__name__, model.id)

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

        self.assertIn("State.{}".format(state.id), objects)
        self.assertIn("City.{}".format(city.id), objects)


if __name__ == "__main__":
    unittest.main()
