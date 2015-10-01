from __future__ import absolute_import
import unittest

import trade


class TestTradeContainer_identify_daytrades_and_common_trades_case_00(
        unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset('some asset')
        self.trade1 = trade.Operation(
                            date='2015-09-21',
                            asset=self.asset,
                            quantity=10,
                            price=2
                        )
        self.trade2 = trade.Operation(
                            date='2015-09-21',
                            asset=self.asset,
                            quantity=-10,
                            price=3
                        )
        self.container = trade.OperationContainer(
            operations=[self.trade1,self.trade2])
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            #trade.prorate_commissions,
            #trade.find_rates_for_positions,
        ]
        #trade.identify_daytrades_and_common_operations(self.container)

    def test_container_should_exist(self):
        self.assertTrue(self.container)

    def test_trades_len_should_be_two(self):
        self.assertEqual(len(self.container.operations), 2)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_10(self):
        self.assertEqual(self.container.operations[1].quantity, -10)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.container.operations[1].price, 3)

    def test_common_trades_len_should_be_0(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertTrue('common operations' not in self.container.positions)

    def test_daytrades_len_should_be_1(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 1)

    def test_check_daytrade_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].asset,
            self.asset
        )

    def test_daytrade_quantity_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].quantity,
            10
        )

    def test_daytrade_buy_price_should_be_2(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].operations[0].price,
            2
        )

    def test_daytrade_buy_quantity_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].operations[0].quantity,
            10
        )

    def test_daytrade_sale_price_should_be_3(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].operations[1].price,
            3
        )

    def test_daytrade_sale_quantity_should_be_minus_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].operations[1].quantity,
            -10
        )

    def test_daytrade_result_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].result,
            10
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_01(
        unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset('some asset')
        self.trade1 = trade.Operation(
                            date='2015-09-21',
                            asset=self.asset,
                            quantity=10,
                            price=2
                        )
        self.trade2 = trade.Operation(
                            date='2015-09-21',
                            asset=self.asset,
                            quantity=-5,
                            price=3
                        )
        self.container = trade.OperationContainer(
            operations=[self.trade1,self.trade2])
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            #trade.prorate_commissions,
            #trade.find_rates_for_positions,
        ]
        #trade.identify_daytrades_and_common_operations(self.container)

    def test_container_should_exist(self):
        self.assertTrue(self.container)

    def test_trades_len_should_be_two(self):
        self.assertEqual(len(self.container.operations), 2)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.container.operations[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(len(self.container.positions['common operations'].keys()), 1)

    def test_check_common_trades0_asset(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset].asset,
            self.asset
        )

    def test_common_trades1_quantity_should_be_5(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset].quantity,
            5
        )

    def test_common_trades1_price_should_be_2(self):
        #trade.identify_daytrades_and_common_operations(self.container)]
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset].price,
            2
        )

    def test_daytrades_len_should_be_1(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 1)

    def test_check_daytrade_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].asset,
            self.asset
        )

    def test_daytrade_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].quantity,
            5
        )

    def test_daytrade_buy_price_should_be_2(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].operations[0].price,
            2
        )

    def test_daytrade_buy_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].operations[0].quantity,
            5
        )

    def test_daytrade_sale_price_should_be_3(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].operations[1].price,
            3
        )

    def test_daytrade_sale_quantity_should_be_minus_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].operations[1].quantity,
            -5
        )

    def test_daytrade_result_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset].result,
            5
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_02(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade.Asset('some asset')
        self.asset2 = trade.Asset('some other asset')
        trade1 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        self.container = trade.OperationContainer(
            operations=[trade1,trade2,trade3])
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            #trade.prorate_commissions,
            #trade.find_rates_for_positions,
        ]
        #trade.identify_daytrades_and_common_operations(self.container)

    def test_container_should_exist(self):
        self.assertTrue(self.container)

    def test_trades_len_should_be_three(self):
        self.assertEqual(len(self.container.operations), 3)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.container.operations[1].price, 3)

    def test_common_trades_len_should_be_2(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(len(self.container.positions['common operations'].keys()), 2)

    def test_check_common_trades0_asset(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_5(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].quantity,
            5
        )

    def test_common_trades0_price_should_be_2(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].price,
            2
        )

    def test_check_common_trades1_asset(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset2].asset,
            self.asset2
        )

    def test_common_trades1_quantity_should_be_minus_5(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset2].quantity,
            -5
        )

    def test_common_trades1_price_should_be_7(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset2].price,
            7
        )

    def test_daytrades_len_should_be_1(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 1)

    def test_check_daytrade_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].asset,
            self.asset1
        )

    def test_daytrade_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].quantity,
            5
        )

    def test_daytrade_buy_price_should_be_2(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].price,
            2
        )

    def test_daytrade_buy_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].quantity,
            5
        )

    def test_daytrade_sale_price_should_be_3(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].price,
            3
        )

    def test_daytrade_sale_quantity_should_be_minus_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].quantity,
            -5
        )

    def test_daytrade_result_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].result,
            5
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_03(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade.Asset('some asset')
        self.asset2 = trade.Asset('some other asset')
        trade1 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        trade4 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=5,
                    price=10
                )
        self.container = trade.OperationContainer(
            operations=[trade1,trade2,trade3,trade4])
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            #trade.prorate_commissions,
            #trade.find_rates_for_positions,
        ]
        #trade.identify_daytrades_and_common_operations(self.container)

    def test_container_should_exist(self):
        self.assertTrue(self.container)

    def test_trades_len_should_be_four(self):
        self.assertEqual(len(self.container.operations), 4)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.container.operations[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(len(self.container.positions['common operations'].keys()), 1)

    def test_check_common_trades0_asset(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_5(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].quantity,
            5
        )

    def test_common_trades0_price_should_be_2(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].price,
            2
        )

    def test_daytrades_len_should_be_2(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 2)

    def test_check_daytrade0_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].quantity,
            5
        )

    def test_daytrade0_buy_price_should_be_2(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].quantity,
            5
        )

    def test_daytrade0_sale_price_should_be_3(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity_should_be_minus_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].quantity,
            -5
        )

    def test_daytrade0_result_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].result,
            5
        )

    def test_check_daytrade1_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].result,
            -15
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_04(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade.Asset('some asset')
        self.asset2 = trade.Asset('some other asset')
        trade1 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        trade4 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=5,
                    price=10
                )
        trade5 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        self.container = trade.OperationContainer(
            operations=[trade1,trade2,trade3,trade4,trade5])
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            #trade.prorate_commissions,
            #trade.find_rates_for_positions,
        ]
        #trade.identify_daytrades_and_common_operations(self.container)

    def test_container_should_exist(self):
        self.assertTrue(self.container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.container.operations), 5)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.container.operations[1].price, 3)

    def test_there_should_be_no_common_trades(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertTrue('common operations' not in self.container.positions)

    def test_daytrades_len_should_be_2(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 2)

    def test_check_daytrade0_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].quantity,
            10
        )

    def test_daytrade0_buy_price_should_be_2(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].quantity,
            10
        )

    def test_daytrade0_sale_price_should_be_3(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity_should_be_minus_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].quantity,
            -10
        )

    def test_daytrade0_result_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].result,
            10
        )

    def test_check_daytrade1_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].result,
            -15
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_05(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade.Asset('some asset')
        self.asset2 = trade.Asset('some other asset')
        trade1 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=10
                )
        trade3 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        trade4 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=5,
                    price=10
                )
        trade5 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=20
                )
        self.container = trade.OperationContainer(
            operations=[trade1,trade2,trade3,trade4,trade5])
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            #trade.prorate_commissions,
            #trade.find_rates_for_positions,
        ]
        #trade.identify_daytrades_and_common_operations(self.container)

    def test_container_should_exist(self):
        self.assertTrue(self.container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.container.operations), 5)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_10(self):
        self.assertEqual(self.container.operations[1].price, 10)

    def test_there_should_be_no_common_trades(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertTrue('common operations' not in self.container.positions)

    def test_daytrades_len_should_be_2(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(len(self.container.positions['daytrades'].keys()), 2)

    def test_check_daytrade0_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].quantity,
            10
        )

    def test_daytrade0_buy_price_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].quantity,
            10
        )

    def test_daytrade0_sale_price_should_be_15(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].price,
            15
        )

    def test_daytrade0_sale_quantity_should_be_minus_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].quantity,
            -10
        )

    def test_daytrade0_result_should_be_130(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].result,
            130
        )

    def test_check_daytrade1_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].result,
            -15
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_06(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade.Asset('some asset')
        self.asset2 = trade.Asset('some other asset')
        trade1 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        trade4 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=5,
                    price=10
                )
        trade5 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=5,
                    price=4
                )
        self.container = trade.OperationContainer(
            operations=[trade1,trade2,trade3,trade4,trade5])
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            #trade.prorate_commissions,
            #trade.find_rates_for_positions,
        ]
        #trade.identify_daytrades_and_common_operations(self.container)

    def test_container_should_exist(self):
        self.assertTrue(self.container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.container.operations), 5)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.container.operations[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(len(self.container.positions['common operations'].keys()), 1)

    def test_check_common_trades0_asset(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_10(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].quantity,
            10
        )

    def test_common_trades0_price_should_be_3(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].price,
            3
        )

    def test_daytrades_len_should_be_2(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            len(self.container.positions['daytrades'].keys()),
            2
        )

    def test_check_daytrade0_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].quantity,
            5
        )

    def test_daytrade0_buy_price_should_be_2(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].quantity,
            5
        )

    def test_daytrade0_sale_price_should_be_3(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity_should_be_minus_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].quantity,
            -5
        )

    def test_daytrade0_result_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].result,
            5
        )

    def test_check_daytrade1_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].result,
            -15
        )


class TestTradeContainer_identify_daytrades_and_common_trades_case_07(
        unittest.TestCase):

    def setUp(self):
        self.asset1 = trade.Asset('some asset')
        self.asset2 = trade.Asset('some other asset')
        self.asset3 = trade.Asset('even other asset')
        trade1 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=10,
                    price=2
                )
        trade2 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=-5,
                    price=3
                )
        trade3 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=-5,
                    price=7
                )
        trade4 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset2,
                    quantity=5,price=10
                )
        trade5 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset1,
                    quantity=5,
                    price=4
                )

        trade6 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset3,
                    quantity=5,
                    price=4
                )
        trade7 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset3,
                    quantity=-5,
                    price=2
                )

        trade8 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset3,
                    quantity=5,
                    price=4
                )
        trade9 = trade.Operation(
                    date='2015-09-21',
                    asset=self.asset3,
                    quantity=-5,
                    price=4
                )

        self.container = trade.OperationContainer(
            operations=[
                trade1,trade2,trade3,trade4,trade5,trade6,trade7,trade8,trade9
            ]
        )
        self.container.fetch_positions_tasks = [
            trade.get_operations_from_exercises,
            trade.identify_daytrades_and_common_operations,
            #trade.prorate_commissions,
            #trade.find_rates_for_positions,
        ]
        #trade.identify_daytrades_and_common_operations(self.container)

    def test_container_should_exist(self):
        self.assertTrue(self.container)

    def test_trades_len_should_be_five(self):
        self.assertEqual(len(self.container.operations), 9)

    def test_trade_0_quantity_should_be_10(self):
        self.assertEqual(self.container.operations[0].quantity, 10)

    def test_trade_0_price_should_be_2(self):
        self.assertEqual(self.container.operations[0].price, 2)

    def test_trade_1_quantity_should_be_minus_5(self):
        self.assertEqual(self.container.operations[1].quantity, -5)

    def test_trade_1_price_should_be_3(self):
        self.assertEqual(self.container.operations[1].price, 3)

    def test_common_trades_len_should_be_1(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(len(self.container.positions['common operations'].keys()), 1)

    def test_check_common_trades0_asset(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].asset,
            self.asset1
        )

    def test_common_trades0_quantity_should_be_10(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].quantity,
            10
        )

    def test_common_trades0_price_should_be_3(self):
        #trade.identify_daytrades_and_common_operations(self.container)
        self.container.fetch_positions()
        self.assertEqual(
            self.container.positions['common operations'][self.asset1].price,
            3
        )

    def test_daytrades_len_should_be_3(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            len(self.container.positions['daytrades'].keys()),
            3
        )

    def test_check_daytrade0_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].asset,
            self.asset1
        )

    def test_daytrade0_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].quantity,
            5
        )

    def test_daytrade0_buy_price_should_be_2(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].price,
            2
        )

    def test_daytrade0_buy_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[0].quantity,
            5
        )

    def test_daytrade0_sale_price_should_be_3(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].price,
            3
        )

    def test_daytrade0_sale_quantity_should_be_minus_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].operations[1].quantity,
            -5
        )

    def test_daytrade0_result_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset1].result,
            5
        )

    def test_check_daytrade1_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].asset,
            self.asset2
        )

    def test_daytrade1_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].quantity,
            5
        )

    def test_daytrade1_buy_price_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].price,
            10
        )

    def test_daytrade1_buy_quantity_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[0].quantity,
            5
        )

    def test_daytrade1_sale_price_should_be_7(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].price,
            7
        )

    def test_daytrade1_sale_quantity_should_be_minus_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].operations[1].quantity,
            -5
        )

    def test_daytrade1_result_should_be_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset2].result,
            -15
        )

    def test_check_daytrade2_asset(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].asset,
            self.asset3
        )

    def test_daytrade2_quantity_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].quantity,
            10
        )

    def test_daytrade2_buy_price_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].operations[0].price,
            4
        )

    def test_daytrade2_buy_quantity_should_be_10(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].operations[0].quantity,
            10
        )

    def test_daytrade2_sale_price_should_be_3(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].operations[1].price,
            3
        )

    def test_daytrade2_sale_quantity_should_be_minus_5(self):
        trade.identify_daytrades_and_common_operations(self.container)
        self.assertEqual(
            self.container.positions['daytrades'][self.asset3].operations[1].quantity,
            -10
        )
