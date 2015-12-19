import sys
import unittest

from haikunator import haikunate


class HaikunatorTests(unittest.TestCase):
    def setUp(self):
        if sys.version_info > (3, 0):
            self.assertRegexp = self.assertRegex
        else:
            self.assertRegexp = self.assertRegexpMatches

    def test_default_use(self):
        self.assertRegexp(haikunate(), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(\\d{4})$")

    def test_hex_use(self):
        self.assertRegexp(haikunate(tokenhex=True), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(.{4})$")

    def test_9digits_use(self):
        self.assertRegexp(haikunate(tokenlength=9), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(\\d{9})$")

    def test_9digitsashex_use(self):
        self.assertRegexp(haikunate(tokenhex=True, tokenlength=9), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(.{9})$")

    def test_wont_return_same(self):
        self.assertNotEqual(haikunate(), haikunate())

    def test_drops_token(self):
        self.assertRegexp(haikunate(tokenlength=0), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))$")

    def test_permits_optional_delimiter(self):
        self.assertRegexp(haikunate(delimiter='.'), "((?:[a-z][a-z]+))(\\.)((?:[a-z][a-z]+))(\\.)(\\d+)$")

    def test_spacedelimiter_and_notoken(self):
        self.assertRegexp(haikunate(delimiter=' ', tokenlength=0), "((?:[a-z][a-z]+))( )((?:[a-z][a-z]+))$")

    def test_onesingleword(self):
        self.assertRegexp(haikunate(delimiter='', tokenlength=0), "((?:[a-z][a-z]+))$")

    def test_customchars(self):
        self.assertRegexp(haikunate(tokenchars='A'), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(AAAA)$")

    def test_return_same_with_seed(self):
        seed = 'testseed'
        self.assertEqual(haikunate(seed=seed), haikunate(seed=seed))


if __name__ == '__main__':
    unittest.main()
