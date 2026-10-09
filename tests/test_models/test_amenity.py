#!/usr/bin/python3
"""Tests for the Amenity class."""

import unittest

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the Amenity class."""

    def test_create_instance(self):
        """Test creating an Amenity instance."""
        amenity = Amenity()

        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity.id, str)
        self.assertIsNone(amenity.name)


if __name__ == "__main__":
    unittest.main()
