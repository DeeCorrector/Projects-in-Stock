from scraper import IRequest, Request
import unittest as ut

class Test_IRequest(ut.TestCase):
    def setUp(self):
        self.instance = IRequest()

    def test_init(self):
        self.assertTrue(type(self.instance), IRequest)

    def test_contains_methods(self):
        try:
            self.instance.get_html()
        except AttributeError:
            self.fail("get_html does not exist!")

class Test_Request(ut.TestCase):
    def setUp(self):
        self.instance = Request("http://www.google.com/")

    def test_contains_valid_fields(self):
        try:
            self.instance.url
        except AttributeError:
            self.fail('Field \'url\' does not exist')

        self.assertFalse(self.instance.url=='')

    def test_inherits_interface(self):
        if not issubclass(Request, IRequest):
            self.fail("Request is not a subclass of its interface")

    def test_implements_get_html(self):
        temp = self.instance.get_html()
        if temp==None:
            self.fail("Request.get_html() returns \'None\'")

        if not type(temp)==str:
            self.fail("Request.get_html() returns a value that is not a string")

        if "<!DOCTYPE" not in temp: self.fail("Request.get_html() returns something that does not contain \'<!DOCTYPE\'")


if __name__ == "__main__":
    ut.main()
