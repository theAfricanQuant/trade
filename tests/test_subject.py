"""Tests for the Subject class."""

from __future__ import absolute_import
import unittest

from trade.subject import Subject


class TestSubject(unittest.TestCase):

    def setUp(self):
        self.subject = Subject("GOOG", {"detail": 1})

    def test_symbol(self):
        """Check the subject symbol."""
        self.assertEqual(self.subject.symbol, "GOOG")

    def test_details(self):
        """Check the subject details."""
        self.assertEqual(self.subject.details, {"detail": 1})


class TestSubjectNoDetails(unittest.TestCase):

    def setUp(self):
        self.subject = Subject("GOOG")

    def test_symbol(self):
        """Check the subject symbol."""
        self.assertEqual(self.subject.symbol, "GOOG")

    def test_details(self):
        """Check the subject details."""
        self.assertEqual(self.subject.details, {})
