import os
import sys
import unittest as ut
from datetime import datetime
import copy
#dependencies for adapter
#Finding the parent directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_dir = base_dir[:-7]
#Plugging the script into Django
sys.path.append(base_dir +"Website/")
os.environ["DJANGO_SETTINGS_MODULE"] = "src.settings"
import django
django.setup()
from web.models import Counselor
from adapter import ScrapeCommand, FindNewCounselorsCommand, CommandFactory, Adapter

#Testing ScrapeCommand
class Test_ScrapeCommand(ut.TestCase):
    def setUp(self):
        self.executionTime = datetime(9999,9,9)
        self.url = "http://example.com"
        self.matchingDictonary = {"content": ".*"}
        self.target = None
        self.instance = ScrapeCommand(self.executionTime,self.url,self.matchingDictonary,self.target)

    #__init__: inits
    def test_inits(self):
        self.instance = ScrapeCommand(self.executionTime,self.url,self.matchingDictonary,self.target)
        self.assertTrue(type(self.instance), ScrapeCommand)
    #__init__: contains _executionTime
    def test_contains_executionTime(self):
        self.instance = ScrapeCommand(self.executionTime,self.url,self.matchingDictonary,self.target)
        self.assertTrue((self.instance.executionTime==self.executionTime),True)

    #__init__: contains _url
    def test_contains_url(self):
        self.instance = ScrapeCommand(self.executionTime,self.url,self.matchingDictonary,self.target)
        self.assertTrue((self.instance.url==self.url),True)
    #__init__: contains _matchDict
    def test_contains_matchingDictonary(self):
        self.instance = ScrapeCommand(self.executionTime,self.url,self.matchingDictonary,self.target)
        self.assertTrue((self.instance.matchingDict==self.matchingDictonary),True)

    #__init__: contains _target
    def test_contains_target(self):
        self.instance = ScrapeCommand(self.executionTime,self.url,self.matchingDictonary,self.target)
        self.assertTrue((self.instance.target==self.target),True)

    #execute: if target is None return result
    def test_returns_when_none(self):
        self.instance = ScrapeCommand(self.executionTime,self.url,self.matchingDictonary,None)
        self.assertTrue(type(self.instance.execute),dict)

    #execute: if target is not None result should be send to target
    def test_sends_to_target(self):
        self.boolean = False
        def mockFunction(x,i):
            self.boolean = True

        self.instance = ScrapeCommand(self.executionTime,self.url,self.matchingDictonary,mockFunction)
        self.instance.execute()
        self.assertTrue(self.boolean, True)
#Testing FindNewCounselorsCommand
    #The following functions of FindNewCounselorsCommand is not
    #tested due to being a part of the implementation:
        #create_new_counselor
        #append_url_format
        #exists_in_database
class Test_FindNewCounselorsCommand(ut.TestCase):
    def setUp(self):
        self.executionTime = datetime(9999,9,9)
    #__init__: inits
    def test_inits(self):
        self.instance = FindNewCounselorsCommand(self.executionTime)
    #__init__: contains _executionTime
    def test_contains_executionTime(self):
        self.instance = FindNewCounselorsCommand(self.executionTime)
        self.assertTrue((self.instance.executionTime == self.executionTime ), True)
    #execute: if the database is empty, it should not be at the end
    #execute: if the database is missing => 1 counselor(s) should be updated with these
    #execute: if the database contains all information, it should be the same as in the end

#CommandFactory
class Test_CommandFactory(ut.TestCase):
    def mock_target(self):
        pass

    #new_ScrapeCommand: returns a ScrapeCommand
    def test_returns_scrape_command(self):
        self.instance = CommandFactory()
        command = self.instance.new_ScrapeCommand(datetime(9999,9,9), "http://example.com", {"content": ".*"}, None)
        self.assertTrue(type(command), ScrapeCommand)

    #new_ScrapeCommand: returns a ScrapeCommand with given _execuntionTIme
    def test_returns_correct_executiontime(self):
        self.instance = CommandFactory()
        command = self.instance.new_ScrapeCommand(datetime(9999,9,9), "http://example.com", {"content": ".*"}, None)
        self.assertTrue(command.executionTime, datetime(9999,9,9))

    #new_ScrapeCommand: returns a ScrapeCommand with given _url
    def test_returns_correct_url(self):
        self.instance = CommandFactory()
        command = self.instance.new_ScrapeCommand(datetime(9999,9,9), "http://example.com", {"content": ".*"}, None)
        self.assertTrue(command.url, "http://example.com")

    #new_ScrapeCommand: returns a ScrapeCommand with given _matchDict
    def test_returns_correct_matchdict(self):
        self.instance = CommandFactory()
        command = self.instance.new_ScrapeCommand(datetime(9999,9,9), "http://example.com", {"content": ".*"}, None)
        self.assertTrue(command.matchingDict, {"content": ".*"})

    #new_ScrapeCommand: returns a ScrapeCommand with given _target
    def test_returns_correct_target(self):
        self.instance = CommandFactory()
        command = self.instance.new_ScrapeCommand(datetime(9999,9,9), "http://example.com", {"content": ".*"}, self.mock_target)
        self.assertTrue(command.target, self.mock_target)


#Adapter
class Test_Adapter(ut.TestCase):
    #The following methods will not be tested due to being a part of the implementation:
        #updatedb
        #convert_bad_encodings

    #__init__: inits
    def test_inits(self):
        self.instance = Adapter()
        self.assertTrue(type(self.instance),Adapter)

    #update_all_now: every counselor is updated
    #update_all_now: if a counselor is outdated it should be updated at end
    #def test_updates_outdated_counselor(self):
    #    self.instance = Adapter()
    #    mockCounselor = Counselor()
    #    mockCounselor.name = "name"
    #    mockCounselor.email = "email"
    #    mockCounselor.office = "office"
    #    mockCounselor.studyArea = "study area"
    #    mockCounselor.url = "http://diku.dk/english/staff/vip/?pure=en/persons/172243"
    #    mockCounselor.save()

    #    beforeCounselor = copy.deepcopy(mockCounselor)
    #    self.instance.update_all_now()
    #    afterCounselor = copy.deepcopy(mockCounselor)
    #    mockCounselor.delete()
    #    self.assertTrue((beforeCounselor != afterCounselor),True)


    #update_now: the given counselor is updated
    #update_now: if the given counselor is outdated it should be updated at end
    #update_now: if the given counselor is up-to-date no changes should be made

    #schedule_update: if the given time is reached, the given counselor should be updated
    #schedule_update: if the given time has not been reached, the given counselor should not be updated

    #get_scheduled_updates: returns a list of commands

    #delete_scheduled_update: if cmdIndex is in range, the given command should be deleted from que
    #delete_scheduled_update: if cmdIndex is out of range, the que should be the same at the end

    #clear_all_scheduled_updates: if the que contains anything it should not at the end
    #clear_all_scheduled_updates: if the que does not contain anything nothing should happen

if __name__ == "__main__":
    ut.main()
