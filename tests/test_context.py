"""Tests for the Context class."""

from __future__ import absolute_import
import unittest

from trade.subject import Subject
from trade.occurrence import Occurrence
from trade.context import Context


def task_1(context):
    """A sample context task.
    
    This task copies the occurrences in Context.occurrences to
    Context.contextualized.
    """
    for occurrence in context.occurrences:
        context.contextualized.append(occurrence)


class TestContext(unittest.TestCase):

    def setUp(self):
        subject = Subject("GOOG", {})
        self.occurrence = Occurrence(
        	subject,
        	"2018-01-02 00:00:00",
        	{"quantity": 1, "value": 1}
        )
        self.context = Context([self.occurrence], [task_1])

    def test_context_initial_state(self):
        """Initial state of the Context.contextualize should be []."""
        self.assertEqual(self.context.contextualized, [])

    def test_apply(self):
        """Context.apply() method should run the sample context task."""
        self.context.apply()
        self.assertEqual(self.context.contextualized, [self.occurrence])
