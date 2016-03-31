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
        self.instance = Request("www.test.testing/testing.html")

    def test_contains_valid_fields(self):
        try:
            self.instance.url
        except AttributeError:
            self.fail('Field \'url\' does not exist')

        self.assertFalse(self.instance.url=='')

    def test_inherits_interface(self):
        self.assertEquals(type(self.instance), IRequest)


if __name__ == "__main__":
    ut.main()
