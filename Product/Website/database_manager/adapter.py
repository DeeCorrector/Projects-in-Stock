from ...CommandManager.commandmanager import CommandManager, ICommand
from Scraper.scraper import Scraper
import re
import datetime

#for testing purposes
counselor_match_dict = {"header": r"<h1 class='site-title'>.*?</h1>"}

class ScrapeCommand (ICommand):
    def __init__(self,_executionTime, _url, _match_dict, _target ):
        super().__init__(_executionTime)
        self.url = _url
        self.matching_dict = _match_dict
        self.target = _target

    def execute(self):
        my_scraper = Scraper(self.url,self.matching_dict)
        result = my_scraper.Scrape()
        self.target(result)

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
    #schedule db_update at specific point in time
    def schedule_update(self,datetime,counselor):
        command = self.my_commandFactory.new_ScrapeCommand(datetime,couselor.url,counselor_match_dict,self.updatedb)
        self.my_commandmanager.enqueue_command(command)

    def updatedb(self,info_dict):
        print (info_dict)

    #get all scheduled db_updates
    def get_scheduled_updates(self):
        return self.my_commandmanager.commandQueue

    #Delete specific db_update
    def delete_scheduled_update(self,cmd_id):
        self.my_commandmanager.delete_command(cmd_id)
    #clear all scheduled db_update
    #Update database

class MockCounselor():
    def __init__(self,_url):
        self.url = _url

if __name__ == "__main__":
    a = Adapter()
    a.schedule_update(datetime.datetime.now() + datetime.timedelta(seconds=1),MockCounselor("http://www.test.org/"))
