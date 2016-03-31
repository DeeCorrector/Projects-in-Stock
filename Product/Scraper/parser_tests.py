from scraper import IParser, Parser
import unittest as ut

class Test_IParser(ut.TestCase):
  def setUp(self):
      self.instance = IParser()

  def test_init(self):
      self.assertTrue(type(self.instance),IParser)

  def test_contains_methods(self):
      try:
          self.instance.parse_html()
      except AttributeError:
          self.fail("parse_html() does not exist!")

class Test_Parser(ut.TestCase):
  def setUp(self):
      self.instance = Parser("html",{})

  def test_init(self):
      self.assertTrue(type(self.instance),Parser)

  def test_contains_valid_fields(self):
      try:
          self.instance.html
      except AttributeError:
          self.fail("field \'html\' does not exist")

      self.assertFalse(self.instance.html =="")

  def test_inherits_interface(self):
      if not issubclass(Parser,IParser):
          self.fail("Parser does not inherit from IParser")

#                            !!!Beware!!!
#                        Actually tests if the IParser
#                        contains the get_html method.
#                        We will have to change this,
#                        issues has been submitted to
#                        github.

  def test_contains_methods(self):
      try:
          self.instance.parse_html()
      except AttributeError:
          self.fail("parse_html() does not exist!")

  def test_get_html_returns_dictionary(self):
      self.assertEquals(type(self.instance.parse_html()),dict)


if __name__ == "__main__":
  ut.main()
