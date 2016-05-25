import unittest as ut
from scraper import Scraper

class TestScraper(ut.TestCase):
    def test_init(self):
        instance = Scraper('http://www.diku.dk/', {})
        try:
            instance.requester
        except AttributeError:
            self.fail("Scraper contains no requester")

        try:
            instance.parser
        except AttributeError:
            self.fail("Scraper contains no parser")


if __name__ == "__main__":
    ut.main()
