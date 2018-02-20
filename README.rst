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
A *occurrence* may be the purchase of shares of a corporation, updating the holder's
situation.


A subject may relate to none or many subjects
---------------------------------------------
The subject of an occurrence may be related to some underlyng subject (like it is with a *put option*,
for example); Occurrences with this subject may have effects on its underlying subjects.


A *context* may have its own rules
----------------------------------
*Contexts* are groups of operations.

A *context* may be a situation where daytrades should be identified.

A *context* may also involve taxes and other costs.


Extending the framework
-----------------------

**trade** can be extended with new types of *occurrences* and *subjects*.
New *context rules* can be created. Look at the examples.


You can try it `live <https://python-trade.appspot.com>`_.


Quickstart
----------

An example of the JSON interfacem using the **fetch_daytrades** context rule:

.. code:: python

    from trade import trade
    from trade.trade_json import TradeJSON


    interface = TradeJSON(
        [trade.fetch_daytrades],
        {
            'Asset': trade.Asset,
            'Operation': trade.Operation,
        }
    )

    json_input = '''{
        "subjects": {
            "GOOG": {
                "type": "Asset",
                "name": "Google Inc"
            },
            "AAPL": {
                "type": "Asset",
                "name": "Apple, Inc."
            }
        },
        "occurrences": [
            {
                "type": "Operation",
                "subject": "AAPL",
                "date": "2015-11-10",
                "quantity": 10,
                "price": 120.15
            },
            {
                "type": "Operation",
                "subject": "GOOG",
                "date": "2015-11-10",
                "quantity": 10,
                "price": 724.89
            },
            {
                "type": "Operation",
                "subject": "GOOG",
                "date": "2015-11-10",
                "quantity": -5,
                "price": 724.98
            }
        ],
        "initial state": {
            "AAPL": {
                "date": "2015-10-09",
                "quantity": 92,
                "price": 119.27,
                "results": {"trades": 5021.72}
            }
        }
    }'''

    json_output = interface.get_trade_results(json_input)

    print(json_output)
    #$ {
    #  "assets": {
    #    "AAPL": {
    #      "states": {
    #        "2015-10-09": {
    #          "price": 119.27,
    #          "quantity": 92,
    #          "results": {
    #            "trades": 5021.7200000000003
    #          }
    #        },
    #        "2015-11-10": {
    #          "price": 119.35627450980392,
    #          "quantity": 102,
    #          "results": {
    #            "trades": 5021.7200000000003
    #          }
    #        }
    #      },
    #      "totals": {
    #        "daytrades": 0,
    #        "operations": 1,
    #        "purchases": 1,
    #        "results": {
    #          "trades": 5021.7200000000003
    #        },
    #        "sales": 0
    #      }
    #    },
    #    "GOOG": {
    #      "states": {
    #        "2015-11-10": {
    #          "price": 724.88999999999999,
    #          "quantity": 5,
    #          "results": {
    #            "daytrades": 0.45000000000027285
    #          }
    #        }
    #      },
    #      "totals": {
    #        "daytrades": 1,
    #        "operations": 2,
    #        "purchases": 1,
    #        "results": {
    #          "daytrades": 0.45000000000027285
    #        },
    #        "sales": 1
    #      }
    #    }
    #  },
    #  "totals": {
    #    "daytrades": 1,
    #    "operations": 3,
    #    "purchases": {
    #      "operations": 2,
    #      "volume": 8450.3999999999996
    #    },
    #    "results": {
    #      "daytrades": 0.45000000000027285,
    #      "trades": 5021.7200000000003
    #    },
    #    "sales": {
    #      "operations": 1,
    #      "volume": 3624.9000000000001
    #    }
    #  }
    #}


Compatibility
-------------

trade is compatible with Python 2.7, 3.3, 3.4, 3.5 and 3.6.


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
