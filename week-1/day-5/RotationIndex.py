import unittest

def find_rotation_point(words):
    starting_word = words[0]
    last_index = 0
    first_index = len(words)-1
    
    while last_index<first_index:
        guess_word = last_index+((first_index-last_index)/2)
        if words[guess_word] >= starting_word:
            last_index = guess_word

        else:
            first_index = guess_word
        if last_index +1 == first_index:
            return first_index
    return -1

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

   


unittest.main(verbosity=2)
        
