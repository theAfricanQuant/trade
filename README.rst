trade
=====

| Copyright (c) 2015-2018 Rafael da Silva Rocha
| https://python-trade.appspot.com
| https://github.com/rochars/trade

--------------

|Build| |Windows Build| |Coverage Status| |Scrutinizer| |Python Versions| |Live Demo|


Installation
------------

    $ pip install trade


trade
-----
**trade** is a framework for the creation of financial applications.


It uses the concept of *holders*, *subjects* and *occurrences*
--------------------------------------------------------------
A *subject* represent anything that can be traded.

An *occurrence* represent anything that affects one or more subjects.

A *holder* is someone who owns subjects and may perform *occurrences*.

*Occurrences* may happen without intervention of the holder.

*Occurrences* may occur alone or in *contexts*, like a group of operations performed within a day.


Different subjects may have different attributes
------------------------------------------------
A *subject* may be the share of a corporation, wooden logs, livestock and so on.


An occurrence involves one or many subjects
-------------------------------------------


A subject may relate to none or many subjects
---------------------------------------------
The subject of an occurrence may be related to some underlyng subject (like it is with a *put option*,
for example); Occurrences with this subject may have effects on its underlying subjects.


A *context* may have its own rules
----------------------------------
*Contexts* are groups of occurrences.

A *context* may be a situation where daytrades should be identified.

A *context* may also involve taxes and other costs altering the details of the occurrences.


Extending the framework
-----------------------

**trade** can be extended with new types of *occurrences* and *subjects*.
New *context rules* can be created. Look at the examples.


You can try it `live <https://python-trade.appspot.com>`_.


Use:
----

A example without the use of contexts:

.. code:: python

	from trade.holder import Holder
	from trade.occurrence import Occurrence
	from trade.subject import Subject

	# create a holder
	holder = Holder()

	# define some subject
	some_asset = Subject('AST1', 'Some Asset')

	# create an occurrence with that subject.
	# In this example, a purchase of 100 units of the asset,
	# for the price of $20.
	some_occurrence = Occurrence(
			subject=some_asset,
			date='2018-01-02',
			quantity=100,
			price=20
		)

	# pass it to the holder
	holder.accumulate(some_occurrence)

	# check the holder state:
	for subject, subject_details in holder.subjects.items():
		print(subject)
		print(subject_details.state)

	# create some other occurrence with that subject.
	# In this example, a sale of 20 units of the asset,
	# for the price of $30.
	other_occurrence = Occurrence(
			subject=some_asset,
			date='2018-01-02',
			quantity=-20,
			price=30
		)
	holder.accumulate(other_occurrence)

	# check the holder state. It should show a change in quantity
	# and some profit:
	for subject, subject_details in holder.subjects.items():
		print(subject)
		print(subject_details.state)


	# create some other occurrence with that subject.
	# Now a purchase of 10 units of the asset, for the
	# price of $20.
	another_occurrence = Occurrence(
			subject=some_asset,
			date='2018-01-02',
			quantity=10,
			price=25
		)
	holder.accumulate(another_occurrence)

	# check the holder state. It should show a change in quantity
	# and in the value of the subject:
	for subject, subject_details in holder.subjects.items():
		print(subject)
		print(subject_details.state)



License
-------

Copyright (c) 2015-2018 Rafael da Silva Rocha

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
“Software”), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



.. |Build| image:: https://img.shields.io/travis/rochars/trade.svg?label=unix%20build
   :target: https://travis-ci.org/rochars/trade
.. |Windows Build| image:: https://img.shields.io/appveyor/ci/rochars/trade.svg?label=windows%20build
   :target: https://ci.appveyor.com/project/rochars/trade
.. |Coverage Status| image:: https://coveralls.io/repos/rochars/trade/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/rochars/trade?branch=master
.. |Scrutinizer| image:: https://scrutinizer-ci.com/g/rochars/trade/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/rochars/trade/
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/trade.png
   :target: https://pypi.python.org/pypi/trade/
.. |Live Demo| image:: https://img.shields.io/badge/try-live%20demo-blue.png
   :target: https://python-trade.appspot.com/
.. |Documentation| image:: https://readthedocs.org/projects/trade/badge/
   :target: http://trade.readthedocs.org/en/latest/
.. |License| image:: https://img.shields.io/pypi/l/trade.png
   :target: https://opensource.org/licenses/MIT
