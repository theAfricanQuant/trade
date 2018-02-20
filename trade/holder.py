"""Holder

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


class Holder(object):
    """A holder of subjects.

    It receives Occurrence objects and update its accumulators
    with them. The state of each subject in the Portfolio accumulators
    are updated according to the occurrence.

    Attributes:
        subjects: A dict {Subject.symbol: Accumulator}.
    """

    def __init__(self, state=None):
        self.subjects = {}
        if state:
            for subject, subject_state in state.items():
                self.subjects[subject.symbol] = Accumulator(
                    subject,
                    subject_state
                )

    def accumulate(self, occurrence):
        """Update the state of the Portfolio with an occurrence."""
        occurrence.update_portfolio(self)
        self.accumulate_occurrence(occurrence)

    def accumulate_occurrence(self, occurrence):
        """Accumulates an occurrence on its corresponding accumulator."""
        if occurrence.subject.symbol not in self.subjects:
            self.subjects[occurrence.subject.symbol] = Accumulator(
                occurrence.subject
            )
        self.subjects[occurrence.subject.symbol].accumulate(occurrence)


class Accumulator(object):
    """An accumulator of occurrences with an subject.

    Accumulators represent the situation of a subject belonging to a
    Holder.

    A Holder have multiple Accumulator instances on its subjects list,
    one for each subject the holder have.

    An Accumulator object accumualates occurrences of a single subject.

    Attributes:
        subject: An subject instance, the subject whose data is being
            accumulated.
        date: A string 'YYYY-mm-dd' representing the date of the last
            status change of the accumulator.
        state: A dictionary with the initial state of this accumulator.
        logging: A boolean indicating if the accumulator should log
            the data passed to accumulate().
        log: A dict with all the occurrences performed with the subject,
            provided that self.logging is True.
    """

    def __init__(self, subject, state=None, logging=True):
        self.log = {}
        self.date = None
        if state:
            self.set_initial_state(state)
        else:
            self.state = subject.get_default_state()
        self.subject = subject
        self.logging = logging

    def set_initial_state(self, state):
        """Set the initial state of the Accumulator object."""
        self.state = copy.deepcopy(state)
        if 'date' in state:
            self.set_initial_state_by_date(state)

    def set_initial_state_by_date(self, state):
        """Set the initial state of the Accumulator object by date."""
        self.state.pop('date', None)
        self.date = state['date']
        self.log[state['date']] = {}
        for key in [x for x in state.keys() if x != 'date']:
            self.log[state['date']][key] = state[key]

    def accumulate(self, occurrence):
        """Accumulates an occurrence."""
        occurrence.update_accumulator(self)
        if self.logging:
            self.log_occurrence(occurrence)

    def log_occurrence(self, operation):
        """Log the state of the accumulator.

        If logging, this method is called behind the scenes every
        time accumulate() is called. The states are logged by day
        like this:
        {
            'YYYY-mm-dd': state,
            ...
        }
        """
        self.log[operation.date] = copy.deepcopy(self.state)
