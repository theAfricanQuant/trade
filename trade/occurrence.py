"""Occurrence

Copyright (c) 2015-2017 Rafael da Silva Rocha

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
from __future__ import division

import math

from . utils import (
    average_price,
    same_sign,
    merge_operations,
    find_purchase_and_sale
)

class Occurrence(object):
    """An occurrence with a subject in a date.

    Class Attributes:
        update_position: A boolean indication if the operation should
            update the position of the accumulator or not.
        update_results: A boolean indication if the operation should
            update the results of the accumulator or not.
        update_container: A boolean indication if the operation should
            update the context in a OperationContainer or not.

    Attributes:
        date: A string 'YYYY-mm-dd', the date the operation occurred.
        subject: An Asset instance, the asset that is being traded.
        quantity: A number representing the quantity being traded.
            Positive quantities represent a purchase.
            Negative quantities represent a sale.
        price: The raw unitary price of the asset being traded.
        commissions: A dict of discounts. String keys and float values
            representing the name of the discounts and the values
            to be deducted added to the the operation value.
        operations: A list of underlying occurrences that the
            might may have.
    """

    # By default every operation
    # updates the accumulator position
    update_position = True

    # By default every operation
    # updates the accumulator results
    update_results = True

    # By default every operation updates
    # the OperationContainer positions
    update_container = True

    def __init__(self, subject=None, date=None, **kwargs):
        #super(Operation, self).__init__(subject, date)
        self.subject = subject
        self.date = date
        self.quantity = kwargs.get('quantity', 0)
        self.price = kwargs.get('price', 0)
        self.commissions = kwargs.get('commissions', {})
        self.raw_results = kwargs.get('raw_results', {})
        self.operations = kwargs.get('operations', [])

    def update_portfolio(self, portfolio):
        """Should udpate the portfolio state.

        This is method is called by the Portfolio object when it accumulates
        the Occurrence. It is called before the accumulation occurs, so the
        Occurrence is free to manipulate the Portfolio data before it is passed
        to its subject corresponding Accumulator.
        """
        pass

    @property
    def results(self):
        """Returns the results associated with the operation."""
        return self.raw_results

    @property
    def real_value(self):
        """Returns the quantity * the real price of the operation."""
        return self.quantity * self.real_price

    @property
    def real_price(self):
        """Returns the real price of the operation.

        The real price is the price with all commission and costs
        already deducted or added.
        """
        return self.price + math.copysign(
            self.total_commissions / self.quantity,
            self.quantity
        )

    @property
    def total_commissions(self):
        """Returns the sum of all commissions of this operation."""
        return sum(self.commissions.values())

    @property
    def volume(self):
        """Returns the quantity of the operation * its raw price."""
        return abs(self.quantity) * self.price

    def update_accumulator(self, accumulator):
        """Updates the accumulator with the operation data."""
        if self.need_position_update(accumulator):
            self.update_positions(accumulator)
        if self.update_results:
            self.update_accumulator_results(accumulator)

    def update_accumulator_results(self, accumulator):
        """Updates the results stored in the accumulator."""
        for key, value in self.results.items():
            if key not in accumulator.state['results']:
                accumulator.state['results'][key] = 0
            accumulator.state['results'][key] += value

    def need_position_update(self, accumulator):
        """Check if there is a need to update the position."""
        return (
            self.subject.symbol == accumulator.subject.symbol and
            self.quantity
        )

    def update_position_different_sign(self, accumulator, new_quantity):
        """Update when the operation and position have opposing signs."""
        # if we are trading more than the amount in the portfolio
        # the result will be calculated based only on what was traded
        # (the rest creates a new position)
        if abs(self.quantity) > abs(accumulator.state['quantity']):
            result_quantity = accumulator.state['quantity'] * -1
        else:
            result_quantity = self.quantity
        results = \
            result_quantity * accumulator.state['price'] - \
            result_quantity * self.real_price
        if results:
            self.results['trades'] = results
        if not same_sign(accumulator.state['quantity'], new_quantity):
            accumulator.state['price'] = self.real_price

    def update_position_same_sign(self, accumulator):
        """Update position when operation and position have the same sign."""
        accumulator.state['price'] = average_price(
            accumulator.state['quantity'],
            accumulator.state['price'],
            self.quantity,
            self.real_price
        )

    def update_positions(self, accumulator):
        """Updates the state of the asset with the operation data."""
        new_quantity = accumulator.state['quantity'] + self.quantity
        # same sign, udpate the cost
        if same_sign(accumulator.state['quantity'], self.quantity):
            self.update_position_same_sign(accumulator)
        # different signs, update the results
        elif accumulator.state['quantity'] != 0:
            self.update_position_different_sign(accumulator, new_quantity)
        else:
            accumulator.state['price'] = self.real_price
        accumulator.state['quantity'] = new_quantity
        if not accumulator.state['quantity']:
            accumulator.state['price'] = 0

    '''
    def update_accumulator(self, accumulator):
        """Should udpate the accumulator state.

        This method is called before the Accumulator log its current state.
        """
        pass
    '''