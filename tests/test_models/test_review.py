#!/usr/bin/python3
"""Tests for the Review class."""

import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Review class."""

    def test_create_instance(self):
        """Test creating a Review instance."""
        review = Review()

        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review.id, str)

        self.assertIsNone(review.text)
        self.assertIsNone(review.place_id)
        self.assertIsNone(review.user_id)


if __name__ == "__main__":
    unittest.main()
