#To make the commandmanager and the scraper importable,
#run "export PYTHONPATH="${PYTHONPATH}:PATH/TO/PROJECTS-IN-STOCK/Product/CommandManager/:PATH/TO/PROJECTS-IN-STOCK/Product/Scraper/""
#or if you are using virtualenv add the line to the activate file and reactivate the environment.
from commandmanager import CommandManager,ICommand
from scraper import Scraper
from web.models import Counselor
import re
import datetime


counselor_match_dict = {"name": "<span class=\"person\">.*</span>",
                        "email": "<span>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+</span>",
                        "office": "<div class=\"address\"><p>.*</p></div>",
                        "study area": "<h2 class=\"title\">M.*</h2><ul class=\"relations organisations\">.*</ul>"}

class ScrapeCommand (ICommand):
    def __init__(self,_executionTime, _url, _match_dict, _target ):
        super().__init__(_executionTime)
        self.url = _url
        self.matching_dict = _match_dict
        self.target = _target

    def execute(self):
        my_scraper = Scraper(self.url,self.matching_dict)
        result = my_scraper.scrape()
        self.target(result, self.url)

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
            db_target.name = info_dict["name"]
            db_target.email = info_dict["email"]
            db_target.office = info_dict["office"]
            db.target.study_area = info_dict["study area"]
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
    target = models.Counselor.objects.get(name="TEMP")
    my_adapter = Adapter()
    my_adapter.update_now(target)
