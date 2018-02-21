trade Application Example
=========================

| Copyright (c) 2016 Rafael da Silva Rocha
| https://python-trade.appspot.com
| https://github.com/rochars/trade
| http://trade.readthedocs.org


trade App Example
-----------------

A sample application using the **trade** framework. It contains implementations
for calls, puts, stock splits, reverse stock splits and bonus shares.

Check the tests to see how things work.


Quickstart
----------

An example of a JSON interface using the **fetch_daytrades** context rule.

.. code:: python
    
    from trade import context
    from trade.subject import Subject
    from trade.occurrence import Occurrence
    from trade.trade_json import TradeJSON


    interface = TradeJSON(
        [context.fetch_daytrades],
        {
            'Asset': Subject,
            'Operation': Occurrence,
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


License
-------

Copyright (c) 2016 Rafael da Silva Rocha

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
