"""Tests for the Holder class."""

from __future__ import absolute_import
import unittest

from trade.subject import Subject
from trade.occurrence import Occurrence
from trade.holder import Holder


class TestHolder(unittest.TestCase):

    def setUp(self):
        subject = Subject("GOOG", {})
        self.occurrence_1 = Occurrence(
        	subject,
        	"2018-01-02 00:00:00",
        	{"quantity": 1, "value": 1}
        )
        self.occurrence_2 = Occurrence(
            subject,
            "2018-01-02 00:00:00",
            {"quantity": -1, "value": 1}
        )
        self.occurrence_3 = Occurrence(
            subject,
            "2018-01-02 00:00:00",
            {"quantity": 1, "value": 2}
        )
        self.holder = Holder()

    def test_holder_initial_state(self):
        holder = Holder({'test':0})
        self.assertEqual(holder.state, {'test':0})

    def test_holder_1(self):
    	self.holder.trade(self.occurrence_1)
    	self.assertEqual(
    		self.holder.state,
    		{
    			"GOOG": {
    				"quantity": 1,
    				"value": 1
    			}
    		})

    def test_holder_2(self):
        self.holder.trade(self.occurrence_1)
        self.holder.trade(self.occurrence_2)
        self.assertEqual(
            self.holder.state,
            {
                "GOOG": {
                    "quantity": 0,
                    "value": 0
                }
            })

    def test_holder_3(self):
        self.holder.trade(self.occurrence_1)
        self.holder.trade(self.occurrence_2)
        self.holder.trade(self.occurrence_1)
        self.assertEqual(
            self.holder.state,
            {
                "GOOG": {
                    "quantity": 1,
                    "value": 1
                }
            })

    def test_holder_4(self):
        self.holder.trade(self.occurrence_1)
        self.holder.trade(self.occurrence_2)
        self.holder.trade(self.occurrence_1)
        self.holder.trade(self.occurrence_3)
        self.assertEqual(
            self.holder.state,
            {
                "GOOG": {
                    "quantity": 2,
                    "value": 1.5
                }
            })