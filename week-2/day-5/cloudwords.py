import unittest

class WordCloudData(object):
    
    def __init__(self, inpstr):
        self.wrdscnt = {}
        self.passingstringtocountwords(inpstr)

    def passingstringtocountwords(self, inpstr):
        strtindex = 0
        cur_len = 0
        for i, character in enumerate(inpstr):
            if i == len(inpstr) - 1:
                if character.isalpha():
                    cur_len += 1
                if cur_len > 0:
                    curword = inpstr[strtindex:
                        strtindex + cur_len]
                    self.addingtodict(curword)


            elif character == ' ' or character == u'\u2014':
                if cur_len > 0:
                    curword = inpstr[strtindex:
                        strtindex + cur_len]
                    self.addingtodict(curword)
                    cur_len = 0

            elif character == '.':
                if i < len(inpstr) - 1 and inpstr[i + 1] == '.':
                    if cur_len > 0:
                        curword = inpstr[strtindex:
                            strtindex + cur_len]
                        self.addingtodict(curword)
                        cur_len = 0

            elif character.isalpha() or character == '\'':
                if cur_len == 0:
                    strtindex = i
                cur_len += 1

            elif character == '-':
                if i > 0 and inpstr[i - 1].isalpha() and \
                        inpstr[i + 1].isalpha():
                    if cur_len == 0:
                        strtindex = i
                    cur_len += 1
                else:
                    if cur_len > 0:
                        curword = inpstr[strtindex:
                            strtindex + cur_len]
                        self.addingtodict(curword)
                        cur_len = 0


    def addingtodict(self, word):
        if word in self.wordcount:
            self.wordcount[word] += 1

        elif word.lower() in self.wordcount:
            self.wordcount[word.lower()] += 1

        elif word.capitalize() in self.wordcount:
            self.wordcount[word] = 1
            self.wordcount[word] += self.wordcount[word.capitalize()]
            del self.wordcount[word.capitalize()]

        else:
            self.wordcount[word] = 1
        
    
class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.wordcount

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.wordcount

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.wordcount

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.wordcount

        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.wordcount

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.wordcount

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
