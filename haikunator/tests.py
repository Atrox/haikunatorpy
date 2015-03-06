import six
import unittest

from haikunator import haikunate


class HaikunatorTests(unittest.TestCase):
    def test_basics(self):
        six.assertRegex(self, haikunate(), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(\d+)")

if __name__ == '__main__':
    unittest.main()
