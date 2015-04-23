import unittest
import sys
from haikunator import haikunate


class HaikunatorTests(unittest.TestCase):
  def test_default_use(self):
    if (sys.version_info > (3, 0)):
      self.assertRegex(haikunate(), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(\\d{4})$")
    else:
      self.assertRegexpMatches(haikunate(), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(\\d{4})$")

  def test_hex_use(self):
    if (sys.version_info > (3, 0)):
      self.assertRegex(haikunate(tokenHex=True), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(.{4})$")
    else:
      self.assertRegexpMatches(haikunate(tokenHex=True), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(.{4})$")

  def test_9digits_use(self):
    if (sys.version_info > (3, 0)):
      self.assertRegex(haikunate(tokenLength=9), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(\\d{9})$")
    else:
      self.assertRegexpMatches(haikunate(tokenLength=9), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(\\d{9})$")

  def test_9digitsashex_use(self):
    if (sys.version_info > (3, 0)):
      self.assertRegex(haikunate(tokenHex=True, tokenLength=9), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(.{9})$")
    else:
      self.assertRegexpMatches(haikunate(tokenHex=True, tokenLength=9), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(.{9})$")

  def test_wont_return_same(self):
    self.assertNotEqual(haikunate(), haikunate())

  def test_drops_token(self):
    if (sys.version_info > (3, 0)):
      self.assertRegex(haikunate(tokenLength=0), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))$")
    else:
      self.assertRegexpMatches(haikunate(tokenLength=0), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))$")

  def test_permits_optional_delimiter(self):
    if (sys.version_info > (3, 0)):
      self.assertRegex(haikunate(delimiter='.'), "((?:[a-z][a-z]+))(\\.)((?:[a-z][a-z]+))(\\.)(\\d+)$")
    else:
      self.assertRegexpMatches(haikunate(delimiter='.'), "((?:[a-z][a-z]+))(\\.)((?:[a-z][a-z]+))(\\.)(\\d+)$")

  def test_spacedelimiter_and_notoken(self):
    if (sys.version_info > (3, 0)):
      self.assertRegex(haikunate(delimiter=' ', tokenLength=0), "((?:[a-z][a-z]+))( )((?:[a-z][a-z]+))$")
    else:
      self.assertRegexpMatches(haikunate(delimiter=' ', tokenLength=0), "((?:[a-z][a-z]+))( )((?:[a-z][a-z]+))$")

  def test_onesingleword(self):
    if (sys.version_info > (3, 0)):
      self.assertRegex(haikunate(delimiter='', tokenLength=0), "((?:[a-z][a-z]+))$")
    else:
      self.assertRegexpMatches(haikunate(delimiter='', tokenLength=0), "((?:[a-z][a-z]+))$")

  def test_customchars(self):
    if (sys.version_info > (3, 0)):
      self.assertRegex(haikunate(tokenChars='A'), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(AAAA)$")
    else:
      self.assertRegexpMatches(haikunate(tokenChars='A'), "((?:[a-z][a-z]+))(-)((?:[a-z][a-z]+))(-)(AAAA)$")

if __name__ == '__main__':
  unittest.main()
