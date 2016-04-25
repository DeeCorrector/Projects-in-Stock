#import the regular expressions
import re

#import requesting package
import requests

#interface for request element
class IRequest():
  def get_html(self):
      pass
#concrete request class
class Request(IRequest):
    def __init__(self,_url):
        self.url = _url

    def get_html(self):
        response = requests.get(self.url)
        return(response.text)

#Interface for the parser
class IParser():
    def parse_html(self):
        pass

#Parser implementation
class Parser(IParser):
    def __init__(self,_html,_match_dict):
        self.html = _html
        #copying by value to avoid overwriting the given _match_dict in memory
        self.matching_dictonary = _match_dict.copy()
        self.result_dictonary = _match_dict.copy()

    def parse_html(self):
        #removes the html tags from a given string
        def remove_tags(_string):
            string_no_tags = re.sub("<.*?>","",_string)
            return string_no_tags
        #Runs each regex and tries to find matches
        print (self.matching_dictonary)
        for key in self.matching_dictonary:
            matches_list = re.findall(self.matching_dictonary[key],self.html)
            cleaned_matches_list = []
            #removes tags from each result
            for n in matches_list:
                clean_string = remove_tags(n)
                cleaned_matches_list.append(clean_string)

            #Replace dictonary element with the new list
            self.result_dictonary[key] = cleaned_matches_list
        return self.result_dictonary

class _Scraper():
    def __init__(self, _url, _matching_dict):
        self.requester = Request(_url)
        self.parser = Parser("No html retrived yet!", _matching_dict)

    def request(self):
        self.parser.html = self.requester.get_html()

    def parse(self):
        return self.parser.parse_html()

class Scraper(_Scraper):
    def __init__(self, _url, _matching_dict):
        super().__init__(_url,_matching_dict)

    def scrape(self):
        self.request()
        return self.parse()
