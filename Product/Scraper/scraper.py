import requests

class IRequest():
  def get_html(self):
      pass

class Request(IRequest):
    def __init__(self,_url):
        self.url = _url

    def get_html(self):
        response = requests.get(self.url)
        return(response.text)
