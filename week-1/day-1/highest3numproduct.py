import unittest
def highest_product(lst):
    k = len(lst)
    
    if(k<3):
        raise IndexError('A minimum of 3 numbers are required for multiplication')
    
    sortedone = sorted(lst)
    highproduct1 = sortedone[k-1]*sortedone[k-2]*sortedone[k-3]
    highproduct2 = sortedone[k-1]*sortedone[0]*sortedone[1]
    if(highproduct1>highproduct2):
        return highproduct1
    return highproduct2


class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product([1, 1])


unittest.main(verbosity=2)
