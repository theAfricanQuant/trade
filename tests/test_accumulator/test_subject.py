"""Tests for the Subject class.

Copyright (c) 2015 Rafael da Silva Rocha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from __future__ import absolute_import
import unittest

from trade.accumulator import Accumulator
from tests.test_accumulator import fixtures
from trade.accumulator import Subject


class TestSubject(unittest.TestCase):
    """Tests Subject objects."""

    subject = fixtures.SUBJECT

    def setUp(self):
        """Creates a Subject."""
        self.accumulator = Accumulator(self.subject)

    def test_subject_creation(self):
        """Checks if the Subject exists."""
        self.assertTrue(self.subject)

    def test_subject_default_state(self):
        """Test the get_default_state method of the subject."""
        self.assertEqual(
            self.subject.get_default_state(),
            self.subject.default_state
        )

    def test_subject_expiration(self):
        """Test the expire method of the subject."""
        self.accumulator.state = {'some state': 0}
        self.subject.expire(self.accumulator)
        self.assertEqual(
            self.accumulator.state,
            self.subject.default_state
        )
