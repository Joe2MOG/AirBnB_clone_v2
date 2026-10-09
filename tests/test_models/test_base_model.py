#!/usr/bin/python3
"""Tests for the BaseModel class."""

import unittest
from datetime import datetime
from os import getenv
from time import sleep

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""

    def test_create_instance(self):
        """Test creating a BaseModel instance."""
        model = BaseModel()

        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_unique_ids(self):
        """Test that two instances have different IDs."""
        first = BaseModel()
        second = BaseModel()

        self.assertNotEqual(first.id, second.id)

    def test_str(self):
        """Test the string representation."""
        model = BaseModel()
        result = str(model)

        self.assertIn("[BaseModel]", result)
        self.assertIn(model.id, result)

    def test_to_dict(self):
        """Test the dictionary representation."""
        model = BaseModel()
        result = model.to_dict()

        self.assertIsInstance(result, dict)
        self.assertEqual(result["__class__"], "BaseModel")
        self.assertEqual(result["id"], model.id)
        self.assertIsInstance(result["created_at"], str)
        self.assertIsInstance(result["updated_at"], str)
        self.assertNotIn("_sa_instance_state", result)

    def test_recreate_from_dict(self):
        """Test recreating an object from a dictionary."""
        original = BaseModel()
        data = original.to_dict()

        recreated = BaseModel(**data)

        self.assertEqual(recreated.id, original.id)
        self.assertEqual(
            recreated.created_at,
            original.created_at
        )
        self.assertEqual(
            recreated.updated_at,
            original.updated_at
        )

    @unittest.skipIf(
        getenv("HBNB_TYPE_STORAGE") == "db",
        "BaseModel is not a mapped database model"
    )
    def test_save(self):
        """Test that save updates updated_at."""
        model = BaseModel()
        old_updated_at = model.updated_at

        sleep(0.01)
        model.save()

        self.assertGreater(
            model.updated_at,
            old_updated_at
        )


if __name__ == "__main__":
    unittest.main()
