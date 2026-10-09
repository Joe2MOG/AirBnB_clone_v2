#!/usr/bin/python3
"""General model contract tests."""

import unittest
from datetime import datetime
from uuid import UUID

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestModelContracts(unittest.TestCase):
    """Test common contracts across model classes."""

    def test_base_model_id_is_string(self):
        """Test that BaseModel id is a string."""
        model = BaseModel()

        self.assertIsInstance(model.id, str)

    def test_base_model_id_is_valid_uuid(self):
        """Test that BaseModel id contains a valid UUID."""
        model = BaseModel()

        parsed_id = UUID(model.id)

        self.assertEqual(str(parsed_id), model.id)

    def test_created_at_is_datetime(self):
        """Test created_at type."""
        model = BaseModel()

        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test updated_at type."""
        model = BaseModel()

        self.assertIsInstance(model.updated_at, datetime)

    def test_two_models_have_different_ids(self):
        """Test that objects receive unique ids."""
        first = BaseModel()
        second = BaseModel()

        self.assertNotEqual(first.id, second.id)

    def test_to_dict_contains_class(self):
        """Test class name in dictionary representation."""
        model = BaseModel()
        result = model.to_dict()

        self.assertIn("__class__", result)
        self.assertEqual(result["__class__"], "BaseModel")

    def test_to_dict_created_at_is_string(self):
        """Test serialized created_at value."""
        model = BaseModel()
        result = model.to_dict()

        self.assertIsInstance(result["created_at"], str)

    def test_to_dict_updated_at_is_string(self):
        """Test serialized updated_at value."""
        model = BaseModel()
        result = model.to_dict()

        self.assertIsInstance(result["updated_at"], str)

    def test_user_default_email(self):
        """Test User email default."""
        self.assertIsNone(User().email)

    def test_state_default_name(self):
        """Test State name default."""
        self.assertIsNone(State().name)

    def test_city_default_state_id(self):
        """Test City state_id default."""
        self.assertIsNone(City().state_id)

    def test_amenity_default_name(self):
        """Test Amenity name default."""
        self.assertIsNone(Amenity().name)

    def test_place_default_number_rooms(self):
        """Test Place room count before database insertion."""
        self.assertIsNone(Place().number_rooms)

    def test_review_default_text(self):
        """Test Review text default."""
        self.assertIsNone(Review().text)


if __name__ == "__main__":
    unittest.main()
