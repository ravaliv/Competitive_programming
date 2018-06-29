import unittest


class Trie(object):

    def __init__(self):
        self.root_node = {}

    def add_word(self, word):
        pres_node = self.root_node
        is_new_word = False

        
        for c in word:
            if c not in pres_node:
                is_new_word = True
                pres_node[c] = {}
            pres_node = pres_node[c]

        if "End Of Word" not in pres_node:
            is_new_word = True
            pres_node["End Of Word"] = {}

        return is_new_word

    
class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)
