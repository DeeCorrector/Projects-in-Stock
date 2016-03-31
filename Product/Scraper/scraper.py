import requests

class IRequest():
  def get_html(self):
      pass

class Request(IRequest):
    def __init__(self,_url):
        self.url = _url

<<<<<<< HEAD
"""Interface for the parser"""
class IParser():
    def parse_html(self):
        pass

"""Parser implementation"""
class Parser(IParser):
    def __init__(self,_html,_match_dict):
        self.html = _html
        self.matching_dictonary = _match_dict

    def parse_html(self):
        return {}
=======
    def get_html(self):
        response = requests.get(self.url)
        return(response.text)
>>>>>>> f51635fbd6746082ecf45ab05dc3aba10b69bc49
