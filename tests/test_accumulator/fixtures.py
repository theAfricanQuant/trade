"""Fixtures for the tests.

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

from trade.accumulator import Accumulator as accumulator
from trade.accumulator import Subject
from trade.accumulator import Occurrence


class SubjectSubclass0(Subject):
    """A subclass of the Subject class.

    This one have a different default_state.
    """
    default_state = {
        'x': 0,
        'y': 0,
    }


# Subject objects for the tests
SUBJECT = Subject(
    'X', 'Subject X', {'expiration_date':'2019-01-01'}
)

# SubjectSubclass0 objects for the tests
SUBJECT_SUB = SubjectSubclass0(
    'Y', 'Subject Y', {'expiration_date':'2029-01-01'}
)


# Occurrence objects for the tests
OCCURRENCE0_0 = Occurrence(
    SUBJECT, "2015-11-09"
)
OCCURRENCE0_1 = Occurrence(
    SUBJECT, "2015-11-10"
)
