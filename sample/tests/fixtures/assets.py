"""A set of assets for the tests."""

from __future__ import absolute_import

from trade_app.trade.subject import Subject

from trade_app.options import Option


ASSET = Subject(symbol='some asset')

OPTION1 = Option(
    symbol='some option',
    underlying_assets={ASSET: 1},
    expiration_date='2015-10-02'
)
