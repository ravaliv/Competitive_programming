import unittest

def sort_scores(unsorted_scores, highscore):

    scrs = [0 for i in range (highscore+1)]
   
    for scr in unsorted_scores:
        scrs[scr]+=1
    res = []
    for r1 in range (highscore,-1,-1):
        for r2 in range (scrs[r1]):
           
            res.append(r1)
    return res

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
