import six
import unittest

from haikunator import haikunate


class HaikunatorTests(unittest.TestCase):
    def test_default_use(self):
        six.assertRegex(self, haikunate(), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(\\d{4})$")

    def test_hex_use(self):
        six.assertRegex(self, haikunate(tokenHex=True), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(.{4})$")

    def test_9digits_use(self):
        six.assertRegex(self, haikunate(tokenLength=9), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(\\d{9})$")

    def test_9digitsashex_use(self):
        six.assertRegex(self, haikunate(tokenHex=True, tokenLength=9), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(.{9})$")

    def test_wont_return_same(self):
        self.assertNotEqual(haikunate(), haikunate())

    def test_drops_token(self):
        six.assertRegex(self, haikunate(tokenLength=0), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))$")

    def test_permits_optional_delimiter(self):
        six.assertRegex(self, haikunate(delimiter='.'), "((?:[a-z][a-z]+))(\\.)((?:[a-z][a-z]+))(\\.)(\\d+)$")

    def test_spacedelimiter_and_notoken(self):
        six.assertRegex(self, haikunate(delimiter=' ', tokenLength=0), "((?:[a-z][a-z]+))( )((?:[a-z][a-z]+))$")

    def test_onesingleword(self):
        six.assertRegex(self, haikunate(delimiter='', tokenLength=0), "((?:[a-z][a-z]+))$")

    def test_customchars(self):
        six.assertRegex(self, haikunate(tokenChars='A'), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(AAAA)$")

if __name__ == '__main__':
    unittest.main()
