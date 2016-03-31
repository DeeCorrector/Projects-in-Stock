class IRequest():
  def get_html(self):
      pass

class Request(IRequest):
    def __init__(self,_url):
        self.url = _url

#Interface for the parser
class IParser():
    def parse_html(self):
        pass

#Parser implementation
class Parser(IParser):
    def __init__(self,_html,_match_dict):
        self.html = _html
        self.matching_dictonary = _match_dict

    def parse_html(self):
        #removes the html tags from a given string
        def remove_tags(self,_string):
            string_no_tags = re.sub("<.*?>","",_string)
            return string_no_tags

        return {}
