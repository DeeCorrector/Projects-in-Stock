import re
import requests

#interface for request class
class IRequest():
  def get_html(self):
      pass

class Request(IRequest):
    def __init__(self,_url):
        self.url = _url

    def get_html(self):
        response = requests.get(self.url)
        return(response.text)

#Interface for parser class
class IParser():
    def parse_html(self):
        pass

class Parser(IParser):
    def __init__(self,_html,_matchDict):
        self.html = _html

        #copying by value to avoid overwriting the given _match_dict in memory
        self.matchingDictonary = _matchDict.copy()
        self.resultDictonary = _matchDict.copy()

    def parse_html(self):
        def remove_tags(_string):
            stringNoTags = re.sub("<.*?>","",_string)
            return stringNoTags

        def convert_bad_encodings(_string):
            translation_dict = {
                '&#248;': 'ø',
                '&#216;': 'Ø',
                '&#229;': 'å',
                '&#197;':'Å',
                '&#230;':'æ',
                '&#198;':'Æ'
            }

            for key in translation_dict:
                _string = _string.replace(key, translation_dict[key])
            return _string

        #Runs each regex and tries to find matches
        for key in self.matchingDictonary:
            matchesList = re.findall(self.matchingDictonary[key],self.html)
            cleanedMatchesList = []

            for match in matchesList:
                cleanString = convert_bad_encodings(remove_tags(match))
                cleanedMatchesList.append(cleanString)

            #Replace dictonary element with the new list
            self.resultDictonary[key] = cleanedMatchesList
        return self.resultDictonary

class _Scraper():
    def __init__(self, _url, _matchingDict):
        self.requester = Request(_url)
        self.parser = Parser("No html retrived yet!", _matchingDict)

    def request(self):
        self.parser.html = self.requester.get_html()

    def parse(self):
        return self.parser.parse_html()

class Scraper(_Scraper):
    def __init__(self, _url, _matchingDict):
        super().__init__(_url,_matchingDict)

    def scrape(self):
        self.request()
        return self.parse()
