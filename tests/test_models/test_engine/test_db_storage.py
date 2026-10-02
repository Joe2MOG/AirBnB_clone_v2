#!/usr/bin/python3
"""Tests for the DBStorage interface."""

import unittest

from models.base_model import BaseModel
from models.city import City
from models.engine.db_storage import DBStorage
from models.state import State


class TestDBStorage(unittest.TestCase):
    """Test the temporary DBStorage interface."""

    def setUp(self):
        """Create fresh storage before every test."""
        self.storage = DBStorage()

    def test_instance_creation(self):
        """Test creation of a DBStorage instance."""
        self.assertIsInstance(self.storage, DBStorage)

    def test_all_returns_dictionary(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """Test adding an object."""
        model = BaseModel()
        self.storage.new(model)

        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, self.storage.all())

    def test_new_keeps_same_object(self):
        """Test that storage retains the original object."""
        model = BaseModel()
        self.storage.new(model)

        key = "BaseModel.{}".format(model.id)
        self.assertIs(self.storage.all()[key], model)

    def test_all_filters_state(self):
        """Test filtering by State class."""
        state = State()
        city = City()

        self.storage.new(state)
        self.storage.new(city)

        objects = self.storage.all(State)

        self.assertIn("State.{}".format(state.id), objects)
        self.assertNotIn("City.{}".format(city.id), objects)

    def test_all_filters_city(self):
        """Test filtering by City class."""
        state = State()
        city = City()

        self.storage.new(state)
        self.storage.new(city)

        objects = self.storage.all(City)

        self.assertIn("City.{}".format(city.id), objects)
        self.assertNotIn("State.{}".format(state.id), objects)

    def test_delete_object(self):
        """Test deleting a stored object."""
        model = BaseModel()
        self.storage.new(model)

        key = "BaseModel.{}".format(model.id)
        self.storage.delete(model)

        self.assertNotIn(key, self.storage.all())

    def test_delete_none(self):
        """Test deleting None."""
        before = len(self.storage.all())

        self.storage.delete(None)

        self.assertEqual(before, len(self.storage.all()))

    def test_delete_unknown_object(self):
        """Test deleting an object not stored."""
        model = BaseModel()

        self.storage.delete(model)

        self.assertIsInstance(self.storage.all(), dict)

    def test_save_returns_none(self):
        """Test temporary save interface."""
        self.assertIsNone(self.storage.save())

    def test_reload_returns_none(self):
        """Test temporary reload interface."""
        self.assertIsNone(self.storage.reload())

    def test_close_returns_none(self):
        """Test temporary close interface."""
        self.assertIsNone(self.storage.close())


if __name__ == "__main__":
    unittest.main()
