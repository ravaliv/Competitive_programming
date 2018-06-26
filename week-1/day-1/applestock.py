import unittest
def profitcal(apst):
    k = len(apst)
    if k < 2:
        raise ValueError("Atleast two prices are needed to calculate the profit")
    else:
        least = apst[0]
        finalprofit = apst[1]-apst[0]
        for pre in range(1,k):
            pre_cost = apst[pre]
            profit = pre_cost - least
            finalprofit = max(finalprofit,profit)
            least = min(least,pre_cost)
    return finalprofit



class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = profitcal([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = profitcal([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = profitcal([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = profitcal([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = profitcal([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            profitcal([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            profitcal([])

unittest.main(verbosity=2)
    
