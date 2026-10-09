#!/usr/bin/python3
"""Tests for the User class."""

import unittest

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class."""

    def test_create_instance(self):
        """Test creating a User instance."""
        user = User()

        self.assertIsInstance(user, User)
        self.assertIsInstance(user.id, str)

        self.assertIsNone(user.email)
        self.assertIsNone(user.password)
        self.assertIsNone(user.first_name)
        self.assertIsNone(user.last_name)

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        self.assertIsInstance(User(), BaseModel)


if __name__ == "__main__":
    unittest.main()
