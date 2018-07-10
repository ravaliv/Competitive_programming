import unittest

def has_palindrome_permutation(input):
    len_of_str = len(input)
    strcount = {}
    for i in range (len_of_str):
        no = strcount.setdefault(input[i], 0)
        strcount[input[i]]=no+1
        
    if (len_of_str%2==0):
        for r in strcount.keys():
            if (strcount[r]%2!=0):
                return False
    else:
        F = False
        for r in strcount.keys():
            if (strcount[r]%2!=0):
                if(F == True):
                    return False
                else:
                    F = True
    return True

# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
