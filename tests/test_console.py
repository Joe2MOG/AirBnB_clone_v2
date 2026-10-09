#!/usr/bin/python3
"""Tests for console create command parameters."""

import io
import unittest
from contextlib import redirect_stdout
from os import getenv

from console import HBNBCommand
from models import storage


@unittest.skipIf(
    getenv("HBNB_TYPE_STORAGE") == "db",
    "Console parameter tests use FileStorage"
)
class TestConsoleCreate(unittest.TestCase):
    """Test the create command with parameters."""

    def run_create(self, arguments):
        """Run create and return the generated object id."""
        output = io.StringIO()

        with redirect_stdout(output):
            HBNBCommand().do_create(arguments)

        return output.getvalue().strip()

    def test_create_string_parameter(self):
        """Test creating an object with a string parameter."""
        obj_id = self.run_create('State name="California"')

        key = "State.{}".format(obj_id)
        obj = storage.all().get(key)

        self.assertIsNotNone(obj)
        self.assertEqual(obj.name, "California")

    def test_create_string_with_underscores(self):
        """Test that underscores in strings become spaces."""
        obj_id = self.run_create(
            'State name="Lagos_State"'
        )

        key = "State.{}".format(obj_id)
        obj = storage.all().get(key)

        self.assertIsNotNone(obj)
        self.assertEqual(obj.name, "Lagos State")

    def test_create_integer_parameters(self):
        """Test creating an object with integer parameters."""
        obj_id = self.run_create(
            "Place number_rooms=4 "
            "number_bathrooms=2 "
            "max_guest=10 "
            "price_by_night=300"
        )

        key = "Place.{}".format(obj_id)
        obj = storage.all().get(key)

        self.assertIsNotNone(obj)
        self.assertEqual(obj.number_rooms, 4)
        self.assertEqual(obj.number_bathrooms, 2)
        self.assertEqual(obj.max_guest, 10)
        self.assertEqual(obj.price_by_night, 300)

    def test_create_float_parameters(self):
        """Test creating an object with float parameters."""
        obj_id = self.run_create(
            "Place latitude=37.773972 "
            "longitude=-122.431297"
        )

        key = "Place.{}".format(obj_id)
        obj = storage.all().get(key)

        self.assertIsNotNone(obj)
        self.assertEqual(obj.latitude, 37.773972)
        self.assertEqual(obj.longitude, -122.431297)

    def test_create_invalid_parameters_are_skipped(self):
        """Test that invalid parameters do not stop creation."""
        obj_id = self.run_create(
            'State name="California" invalid_parameter'
        )

        key = "State.{}".format(obj_id)
        obj = storage.all().get(key)

        self.assertIsNotNone(obj)
        self.assertEqual(obj.name, "California")
        self.assertFalse(hasattr(obj, "invalid_parameter"))


if __name__ == "__main__":
    unittest.main()
