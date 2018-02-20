"""Subject

Copyright (c) 2015-2018 Rafael da Silva Rocha

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

import copy


class Subject(object):
    """The subject of an occurrence.

    Attributes:
        symbol: A string to identify the subject.
        name: A string representing a readable name for the subject.
        expiration_date: A string 'YYYY-mm-dd' stating a expiration
            date for the subject, if any.
        default_state: a dictionary with the default state of the
            subject.
        underlying_assets: Underlying subject of this subject, if
            any.
    """

    default_state = default_state = {
        'quantity': 0,
        'price': 0,
        'results': {}
    }

    def __init__(self, symbol=None, name=None, expiration_date=None, **kwargs):
        self.symbol = symbol
        self.name = name
        self.expiration_date = expiration_date
        self.underlying_assets = kwargs.get('underlying_assets', {})

    def get_default_state(self):
        """Returns the default state of the subject."""
        return copy.deepcopy(self.default_state)

    def expire(self, accumulator):
        """Expires the subject on the Holder portfolio."""
        accumulator.state = self.get_default_state()
