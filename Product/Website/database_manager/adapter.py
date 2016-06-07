# -*- coding: UTF-8 -*-
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
from web.models import Counselor
django.setup()

#Matching dictonaries
counselorMatchDict = {"name": "<span class=\"person\">.*</span>",
                        "email": "<span>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+</span>",
                        "office": "<div class=\"address\"><p>.*</p></div>",
                        "studyarea": "<h2 class=\"title\">M.*</h2><ul class=\"relations organisations\">.*</ul>"}

employeeListMatchDict = {"url":"\?pure=en\/persons+\/[0-9]+"}

#converts bad ascii encodings to unicode
def convert_bad_encodings(infoDict):
    symbolDict = {
        u'&#248;': u'ø',
        u'&#216;': u'Ø',
        u'&#229;': u'å',
        u'&#197;': u'Å',
        u'&#230;': u'æ',
        u'&#198;': u'Æ'
    }
    for symbol in symbolDict:
        for key in infoDict:
            if not infoDict[key] == []:
                infoDict[key] = [x.replace(symbol, symbolDict[symbol]) for x in infoDict[key] ]
            else:
                infoDict[key] = ["no matches"]
    return infoDict

#Scrapes a single url with a given dict at a given time.
class ScrapeCommand (ICommand):
    def __init__(self,_executionTime, _url, _matchDict, _target ):
        self.executionTime = _executionTime
        self.url = _url
        self.matchingDict = _matchDict
        self.target = _target

    def execute(self):
        myScraper = Scraper(self.url,self.matchingDict)
        result = myScraper.scrape()
        if self.target is None:
            return result
        else:
            self.target(result, self.url)

#Searches KU's page for new counselors using the ScrapeCommand. If it finds new counselors they're added to the database
class FindNewCounselorsCommand (ICommand):
    def __init__(self,_executionTime):
        self.executionTime = _executionTime
        #The site listing all of the employees on Diku
        self.url = "http://diku.dk/english/staff/"

        #This matchDict should get all links to counselors on the page
        self.matchDict = employeeListMatchDict
        self.scrapeCommand = CommandFactory().new_ScrapeCommand(datetime.datetime.now(),self.url,self.matchDict, None)

    def execute(self):
        scrapeResult = self.scrapeCommand.execute()
        urlDictonary = self.append_url_format(scrapeResult)

        for key in urlDictonary:
            url_list = urlDictonary[key]
            for url in url_list:
                if not self.exists_in_database(url):
                    Scraper = CommandFactory().new_ScrapeCommand(datetime.datetime.now(),url,counselorMatchDict, None)
                    self.create_new_counselor(Scraper.execute(),url)

    def create_new_counselor(self,infoDict,url):
        def unlisitfy(_dict):
            i = _dict.copy()
            for key in i:
                if i[key] != []:
                    i[key] = i[key][0]
                else:
                    i[key] = ""
            return i

        infoDict = unlisitfy(convert_bad_encodings(infoDict))

        dbTarget = Counselor()
        dbTarget.name = infoDict["name"]
        dbTarget.email = infoDict["email"]
        dbTarget.office = infoDict["office"]
        dbTarget.studyArea = infoDict["studyarea"]
        dbTarget.url = url
        dbTarget.save()

    def append_url_format(self,inputDictonary):
        resultDictonary = inputDictonary
        for key in inputDictonary:
            workingUrlList = []
            for url in inputDictonary[key]:
                workingUrlList.append("http://diku.dk/english/staff/" + url)
            resultDictonary[key] = workingUrlList
        return resultDictonary

    def exists_in_database(self, _url):
        try:
            counselor = Counselor.objects.get(url = _url).name
        except Counselor.DoesNotExist:
            counselor = None
        return counselor

class CommandFactory():
    def new_ScrapeCommand(self,_executionTime,_url,_matchDict,_target):
        command = ScrapeCommand(_executionTime,_url,_matchDict,_target)
        return command

    def new_FindNewCounselorsCommand(self,_executionTime):
        command = FindNewCounselorsCommand(_executionTime)
        return command

class Adapter():
    def __init__(self):
        self.myCommandmanager = CommandManager()
        self.myCommandFactory = CommandFactory()

    def update_all_now(self):
        for counselor in Counselor.objects.all():
            command = self.myCommandFactory.new_ScrapeCommand(datetime.datetime.now(),counselor.url,counselorMatchDict,self.save_counselor_info)
            self.myCommandmanager.enqueue_command(command)

    def update_now(self, counselor):
        command = self.myCommandFactory.new_ScrapeCommand(datetime.datetime.now(),counselor.url,counselorMatchDict,self.save_counselor_info)
        self.myCommandmanager.enqueue_command(command)

    def schedule_update(self, datetime, counselorUrl):
        command = self.myCommandFactory.new_ScrapeCommand(datetime,counselorUrl,counselorMatchDict,self.save_counselor_info)
        self.myCommandmanager.enqueue_command(command)

    def save_counselor_info(self, infoDict, counselorUrl):
        dbTarget = Counselor.objects.get(url = counselorUrl)
        infoDict = convert_bad_encodings(infoDict)
        if dbTarget != None:
            dbTarget.name = infoDict["name"][0]
            dbTarget.email = infoDict["email"][0]
            dbTarget.office = infoDict["office"][0]
            dbTarget.studyArea = infoDict["studyarea"][0]
            dbTarget.save()

    def find_new_counselors(self, executionTime):
        cmd = self.myCommandFactory.new_FindNewCounselorsCommand(executionTime)
        self.myCommandmanager.enqueue_command(cmd)

    def get_scheduled_updates_info(self):
        info_list = []
        id = 0
        for cmd in self.myCommandmanager.commandQueue:
            command_info_dict = {
            "id": id,
            "name": str(type(cmd).__name__),
            "executionTime": str(cmd.executionTime)
            }
            info_list.append(command_info_dict)
            id += 1
        return info_list

    def delete_scheduled_update(self,cmdIndex):
        self.myCommandmanager.delete_command(cmdIndex)

    def clear_all_scheduled_updates(self):
        self.myCommandmanager.commandQueue = []
