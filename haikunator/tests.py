import sys
import unittest

from haikunator import Haikunator


class HaikunatorTests(unittest.TestCase):
    def setUp(self):
        if sys.version_info > (3, 0):
            self.assertRegexp = self.assertRegex
        else:
            self.assertRegexp = self.assertRegexpMatches

    def test_default_use(self):
        haiku = Haikunator().haikunate()
        self.assertRegexp(haiku, "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(\\d{4})$")

    def test_hex_use(self):
        haiku = Haikunator().haikunate(token_hex=True)
        self.assertRegexp(haiku, "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(.{4})$")

    def test_digits_use(self):
        haiku = Haikunator().haikunate(token_length=9)
        self.assertRegexp(haiku, "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(\\d{9})$")

    def test_digits_as_hex(self):
        haiku = Haikunator().haikunate(token_length=9, token_hex=True)
        self.assertRegexp(haiku, "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(.{9})$")

    def test_drop_token(self):
        haiku = Haikunator().haikunate(token_length=0)
        self.assertRegexp(haiku, "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))$")

    def test_permits_optional_delimiter(self):
        haiku = Haikunator().haikunate(delimiter='.')
        self.assertRegexp(haiku, "((?:[a-z][a-z]+))(\\.)((?:[a-z][a-z]+))(\\.)(\\d+)$")

    def test_without_delimiter_and_token(self):
        haiku = Haikunator().haikunate(delimiter=' ', token_length=0)
        self.assertRegexp(haiku, "((?:[a-z][a-z]+))( )((?:[a-z][a-z]+))$")

    def test_single_word(self):
        haiku = Haikunator().haikunate(delimiter='', token_length=0)
        self.assertRegexp(haiku, "((?:[a-z][a-z]+))$")

    def test_custom_chars(self):
        haiku = Haikunator().haikunate(token_chars='A')
        self.assertRegexp(haiku, "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(AAAA)$")

    def test_wont_return_same(self):
        haikunator = Haikunator()

        self.assertNotEqual(haikunator.haikunate(), haikunator.haikunate())

    def test_return_same_with_seed(self):
        haikunator1 = Haikunator(1234)
        haikunator2 = Haikunator(1234)

        self.assertEqual(haikunator1.haikunate(), haikunator2.haikunate())

    def test_custom_adjectives_nouns(self):
        haikunator = Haikunator()
        haikunator.adjectives = ['red']
        haikunator.nouns = ['reindeer']

        self.assertRegexp(haikunator.haikunate(), '(red)(-)(reindeer)(-)(\\d{4})$')

    def test_empty_adjectives_nouns(self):
        haikunator = Haikunator()
        haikunator.adjectives = []
        haikunator.nouns = []

        haiku = haikunator.haikunate(token_chars='')
        self.assertEqual(haiku, '')


if __name__ == '__main__':
    unittest.main()
