import re
import datetime
import os
import sys
#Finding the parent directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_dir = base_dir[:-7]
#Importing commandmanager and Scraper
sys.path.append(base_dir+"CommandManager/")
sys.path.append(base_dir+"Scraper/")
from commandmanager import CommandManager,ICommand
from scraper import Scraper
#Plugging the script into Django
sys.path.append(base_dir +"Website/")
os.environ["DJANGO_SETTINGS_MODULE"] = "src.settings"
import django
django.setup()

#Matching dictonaries for testing purposes
counselor_match_dict = {"name": "<span class=\"person\">.*</span>",
                        "email": "<span>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+</span>",
                        "office": "<div class=\"address\"><p>.*</p></div>",
                        "study area": "<h2 class=\"title\">M.*</h2><ul class=\"relations organisations\">.*</ul>"}

employee_list_match_dict = {"url":"\?pure=en\/persons+\/[0-9]+"}

#Scrapes a single url with a given dict at a given time.
class ScrapeCommand (ICommand):
    def __init__(self,_executionTime, _url, _match_dict, _target ):
        super().__init__(_executionTime)
        self.url = _url
        self.matching_dict = _match_dict
        self.target = _target

    def execute(self):
        my_scraper = Scraper(self.url,self.matching_dict)
        result = my_scraper.scrape()
        if self.target is None:
            return result
        else:
            self.target(result, self.url)

#Searches KU's page for new counselors using the ScrapeCommand. If it finds new counselors they're added to the database
class FindNewCounselorsCommand (ICommand):
    def init(self,_executionTime):
        super().__init(_executionTime)

    def execute(self):
        #The site listing all of the employees on Diku
        self.url = "http://diku.dk/english/staff/"
        #This match_dict should get all links to counselors on the page
        self.match_dict = employee_list_match_dict
        self.scrape_command = CommandFactory().new_ScrapeCommand(datetime.datetime.now(),self.url,self.match_dict, None)
        result = self.scrape_command.execute()
        print (result)

class UpdateAllCounselors(ICommand):
    pass

class CommandFactory():
    def new_ScrapeCommand(self,_executionTime,_url,_match_dict,_target):
        command = ScrapeCommand(_executionTime,_url,_match_dict,_target)
        return command

class Adapter():
    def __init__(self):
        self.my_commandmanager = CommandManager()
        self.my_commandFactory = CommandFactory()

    def update_all_now(self):
        for c in Counselor.objects.all():
            command = self.my_commandFactory.new_ScrapeCommand(datetime.datetime.now(),c.url,counselor_match_dict,self.updatedb)
            self.my_commandmanager.enqueue_command(command)

    #do db_update now
    def update_now(self, counselor):
        command = self.my_commandFactory.new_ScrapeCommand(datetime.datetime.now(),counselor.url,counselor_match_dict,self.updatedb)
        self.my_commandmanager.enqueue_command(command)

    #schedule db_update at specific point in time
    def schedule_update(self, datetime, counselor):
        command = self.my_commandFactory.new_ScrapeCommand(datetime,counselor.url,counselor_match_dict,self.updatedb)
        self.my_commandmanager.enqueue_command(command)

    #Update database
    def updatedb(self,info_dict, counselor_url):
        db_target = Counselor.objects.get(url = counselor_url)
        if db_target != None:
            db_target.name = info_dict["name"][0]
            db_target.email = info_dict["email"][0]
            db_target.office = info_dict["office"][0]
            db_target.study_area = info_dict["study area"][0]
            db_target.save()

    #get all scheduled db_updates
    def get_scheduled_updates(self):
        return self.my_commandmanager.commandQueue

    #Delete specific db_update
    def delete_scheduled_update(self,cmd_index):
        self.my_commandmanager.delete_command(cmd_index)

    #clear all scheduled db_update
    def clear_all_scheduled_updates(self):
        self.commandmanager.commandQueue = []

if __name__ == "__main__":
    test = FindNewCounselorsCommand(datetime.datetime.now())
    test.execute()
