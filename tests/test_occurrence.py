"""Tests for the Subject class."""

from __future__ import absolute_import
import unittest

from trade.subject import Subject
from trade.occurrence import Occurrence


class TestOccurrence(unittest.TestCase):

    def setUp(self):
        self.subject = Subject("GOOG", {})
        self.occurrence = Occurrence(
        	self.subject,
        	"2018-01-02 00:00:00",
        	{"quantity": 1, "value": 1}
        )

    def test_occurrence_subject(self):
    	self.assertEqual(
    		self.occurrence.subject,
    		self.subject)

    def test_occurrence_date(self):
    	self.assertEqual(
    			self.occurrence.date,
    			"2018-01-02 00:00:00")

    def test_occurrence_details(self):
    	self.assertEqual(
    		self.occurrence.details,
    		{"quantity": 1, "value": 1})
