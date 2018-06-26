import unittest
def indexproduct(nume):
    k = len(nume)
    if k < 2:
        raise IndexError('A minimum of 2 numbers are required for multiplication')
    bf= [None] * k


    p = 1
    for i in range(k):
        bf[i] = p
        p *= nume[i]

    p = 1
    i = k
    for i in range(k-1, -1, -1):
##        print(i)
        bf[i] *= p
        p *= nume[i]

    return bf




class Test(unittest.TestCase):

    def test_small_list(self):
        actual = indexproduct([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = indexproduct([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = indexproduct([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = indexproduct([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = indexproduct([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = indexproduct([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            indexproduct([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            indexproduct([1])




unittest.main(verbosity=2)
