import os
import sys

#dependencies for adapter
#Finding the parent directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_dir = base_dir[:-7]
#Plugging the script into Django
sys.path.append(base_dir +"Website/")
os.environ["DJANGO_SETTINGS_MODULE"] = "src.settings"
import django
from web.models import Counselor
django.setup()

from adapter import ScrapeCommand, FindNewCounselorsCommand, CommandFactory, Adapter 

#Testing ScrapeCommand
    #__init__: inits
    #__init__: contains _executionTime
    #__init__: contains _url
    #__init__: contains _matchDict
    #__init__: contains _target

    #execute: if target is None return result
    #execute: if target is not None result should be send to target

#Testing FindNewCounselorsCommand
    #The following functions of FindNewCounselorsCommand is not
    #tested due to being a part of the implementation:
        #create_new_counselor
        #append_url_format
        #exists_in_database
    #__init__: inits
    #__init__: contains _executionTime
    #execute: if the database is empty, it should not be at the end
    #execute: if the database is missing => 1 counselor(s) should be updated with these
    #execute: if the database contains all information, it should be the same as in the end

#CommandFactory
    #new_ScrapeCommand: returns a ScrapeCommand
    #new_ScrapeCommand: returns a ScrapeCommand with given _execuntionTIme
    #new_ScrapeCommand: returns a ScrapeCommand with given _url
    #new_ScrapeCommand: returns a ScrapeCommand with given _matchDict
    #new_ScrapeCommand: returns a ScrapeCommand with given _target


#Adapter
    #The following methods will not be tested due to being a part of the implementation:
        #updatedb
        #convert_bad_encodings

    #__init__: inits

    #update_all_now: every counselor is updated
    #update_all_now: if a counselor is outdated it should be updated at end

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
