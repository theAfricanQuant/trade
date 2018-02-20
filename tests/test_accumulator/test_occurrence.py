from __future__ import absolute_import
import unittest

from trade.holder import Accumulator
from tests.test_accumulator import fixtures
from trade.occurrence import Occurrence
from trade.subject import Subject

class TestOccurrence(unittest.TestCase):
    """Test the creation of Occurrence objects."""

    subject = fixtures.SUBJECT
    date = "2015-11-09"

    def setUp(self):
        """Creates an Occurrence with a Subject."""
        self.accumulator = Accumulator(self.subject)
        self.occurrence = Occurrence(self.subject, self.date)

    def test_occurrence_creation(self):
        """Occurrence.update_accumulator should return nothing."""
        self.assertFalse(
            self.occurrence.update_accumulator(self.accumulator)
        )
