#!/usr/bin/python3
"""Tests for the State class."""

import unittest

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test the State class."""

    def test_create_instance(self):
        """Test creating a State instance."""
        state = State()

        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state.id, str)
        self.assertIsNone(state.name)


if __name__ == "__main__":
    unittest.main()
