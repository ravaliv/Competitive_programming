import unittest

def get_permutations(input):
    a = []
    input_length = len(input)
    if(input_length==0 or input_length==1):
        return set([input])
    for r in range (input_length):
        n = input[0:r]+input[r+1:input_length]
        rav = get_permutations(n)
        for l in rav:
            a.append(input[r]+l)
    return set(a)

# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
