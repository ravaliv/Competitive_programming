import unittest

def find_repeat(arrList):

    upr = len(arrList)-1
    lwr = 1
    while(lwr<upr):
         mid = (lwr+upr)//2
         llwr= upr
         lwupr = mid
         uplwr = mid+1
         upupr = upr
         ldist = lwupr - llwr+ 1
         c = 0
         for v1 in arrList:
             if(v1>=llwr and v1<=lwupr):
                 c+=1
         if (c>ldist):
             upr = llwr
             upr = lwupr
         else:
             upr = uplwr
             upr = upupr
    return upr

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)