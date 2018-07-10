import unittest

def get_closing_paren(string, openning_index):

    c = 0
    l = len(string)
    for i in range (openning_index+1,l):
        if(string[i]=='('):
            c=c+1;
        elif(string[i]==')'):
            if(c==0):
                return i
            else:
                c=c-1

    raise Exception

# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)
