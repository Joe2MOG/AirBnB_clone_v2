#!/usr/bin/python3
"""Tests for the City class."""

import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City class."""

    def test_create_instance(self):
        """Test creating a City instance."""
        city = City()

        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city.id, str)
        self.assertIsNone(city.name)
        self.assertIsNone(city.state_id)


if __name__ == "__main__":
    unittest.main()
