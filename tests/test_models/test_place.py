#!/usr/bin/python3
"""Tests for the Place class."""

import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test the Place class."""

    def test_create_instance(self):
        """Test creating a Place instance."""
        place = Place()

        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place.id, str)

        self.assertIsNone(place.city_id)
        self.assertIsNone(place.user_id)
        self.assertIsNone(place.name)
        self.assertIsNone(place.description)
        self.assertIsNone(place.number_rooms)
        self.assertIsNone(place.number_bathrooms)
        self.assertIsNone(place.max_guest)
        self.assertIsNone(place.price_by_night)
        self.assertIsNone(place.latitude)
        self.assertIsNone(place.longitude)


if __name__ == "__main__":
    unittest.main()
