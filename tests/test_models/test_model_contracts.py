#!/usr/bin/python3
"""Additional tests for AirBnB model contracts."""

import unittest
import uuid
from datetime import datetime

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestModelContracts(unittest.TestCase):
    """Test common model behavior and default attributes."""

    def test_base_model_id_is_string(self):
        """Test that BaseModel id is a string."""
        self.assertIsInstance(BaseModel().id, str)

    def test_base_model_id_is_valid_uuid(self):
        """Test that BaseModel id contains a valid UUID."""
        model = BaseModel()
        self.assertEqual(str(uuid.UUID(model.id)), model.id)

    def test_created_at_is_datetime(self):
        """Test created_at type."""
        self.assertIsInstance(BaseModel().created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test updated_at type."""
        self.assertIsInstance(BaseModel().updated_at, datetime)

    def test_two_models_have_different_ids(self):
        """Test that objects receive unique ids."""
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_to_dict_contains_class(self):
        """Test class name in dictionary representation."""
        model = BaseModel()
        self.assertEqual(model.to_dict()["__class__"], "BaseModel")

    def test_to_dict_created_at_is_string(self):
        """Test serialized created_at value."""
        model = BaseModel()
        self.assertIsInstance(model.to_dict()["created_at"], str)

    def test_to_dict_updated_at_is_string(self):
        """Test serialized updated_at value."""
        model = BaseModel()
        self.assertIsInstance(model.to_dict()["updated_at"], str)

    def test_user_default_email(self):
        """Test User email default."""
        self.assertEqual(User.email, "")

    def test_state_default_name(self):
        """Test State name default."""
        self.assertEqual(State.name, "")

    def test_city_default_state_id(self):
        """Test City state_id default."""
        self.assertEqual(City.state_id, "")

    def test_amenity_default_name(self):
        """Test Amenity name default."""
        self.assertEqual(Amenity.name, "")

    def test_place_default_number_rooms(self):
        """Test Place room count default."""
        self.assertEqual(Place.number_rooms, 0)

    def test_review_default_text(self):
        """Test Review text default."""
        self.assertEqual(Review.text, "")


if __name__ == "__main__":
    unittest.main()
