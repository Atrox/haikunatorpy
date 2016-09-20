import sys
import unittest

from haikunator import Haikunator


class HaikunatorTests(unittest.TestCase):
    def setUp(self):
        if sys.version_info > (3, 0):
            self.assertRegexp = self.assertRegex
        else:
            self.assertRegexp = self.assertRegexpMatches

    def test_general_functionality(self):
        tests = [
            [{}, '[a-z]+-[a-z]+-[0-9]{4}$'],
            [{'token_hex': True}, '[a-z]+-[a-z]+-[0-f]{4}$'],
            [{'token_length': 9}, '[a-z]+-[a-z]+-[0-9]{9}$'],
            [{'token_length': 9, 'token_hex': True}, '[a-z]+-[a-z]+-[0-f]{9}$'],
            [{'token_length': 0}, '[a-z]+-[a-z]+$'],
            [{'delimiter': '.'}, '[a-z]+.[a-z]+.[0-9]{4}$'],
            [{'token_length': 0, 'delimiter': ' '}, '[a-z]+ [a-z]+'],
            [{'token_length': 0, 'delimiter': ''}, '[a-z]+$'],
            [{'token_chars': 'xyz'}, '[a-z]+-[a-z]+-[x-z]{4}$'],
        ]

        haikunator = Haikunator()
        for test in tests:
            self.assertRegexp(haikunator.haikunate(**test[0]), test[1])

    def test_wont_return_same(self):
        haikunator = Haikunator()

        self.assertNotEqual(haikunator.haikunate(), haikunator.haikunate())

    def test_return_same_with_seed(self):
        seed = 'definitively random seed'

        h1 = Haikunator(seed=seed)
        h2 = Haikunator(seed=seed)

        self.assertEqual(h1.haikunate(), h2.haikunate())
        self.assertEqual(h1.haikunate(), h2.haikunate())

    def test_custom_adjectives_nouns(self):
        haikunator = Haikunator(
            adjectives=['adjective'],
            nouns=['noun']
        )

        self.assertRegexp(haikunator.haikunate(), 'adjective-noun-\d{4}$')

    def test_empty_adjectives_nouns(self):
        haikunator = Haikunator(
            adjectives=[],
            nouns=[]
        )

        self.assertEqual(haikunator.haikunate(token_chars=''), '')


if __name__ == '__main__':
    unittest.main()
