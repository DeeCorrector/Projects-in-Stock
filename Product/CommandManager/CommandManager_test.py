from commandmanager import ICommand, CommandManager
from datetime import datetime, timedelta
import unittest as ut
import copy

#Test af ICommand
class Test_ICommand(ut.TestCase):

    def setUp(self):
        self.instance = ICommand(datetime.now())

    #__init__: inits
    def test_init(self):
        self.assertTrue(type(self.instance), ICommand)

    #__init__: contains method execute()
    def test_has_execute(self):
        try:
            self.instance.execute()
        except AttributeError:
            self.fail("execute does not exist!")

#Test af CommandManager
class Test_CommandManager(ut.TestCase):
    def setUp(self):
        self.instance = CommandManager()

    #__init__: inits
    def test_init(self):
        self.instance = CommandManager()
        self.assertTrue(type(self.instance),CommandManager)

    #__init__: contains commandQueue
    def test_contains_commandQueue(self):
        self.instance = CommandManager()
        self.assertTrue(type(self.instance.commandQueue),list)

    #__init__: commandQueue is empty on init
    def test_is_commandQueue_empty(self):
        self.instance = CommandManager()

    #__init__: contains myTimer
    def test_contains_myTimer(self):
        self.instance = CommandManager()
        self.assertTrue(type(self.instance.myTimer),datetime)

    #enqueue_command: commandQueue is +1 longer after enqueue_command
    def test_que_is_longer(self):
        self.instance = CommandManager()
        startLength = len(self.instance.commandQueue)
        command = ICommand(datetime(2017,1,5))
        self.instance.enqueue_command(command)
        endLength = len(self.instance.commandQueue)

        self.assertTrue((startLength != endLength), True)


    #enqueue_command: commandQueue contains the queued command
    def test_que_contains_new_command(self):
        self.instance = CommandManager()
        command = ICommand(datetime(2017,1,5))
        self.instance.enqueue_command(command)
        self.assertTrue((command in self.instance.commandQueue), True)

    #delete_command: commandQueue is -1 longer after delete_command
    def test_que_is_shorter(self):
        self.instance = CommandManager()
        command = ICommand(datetime(2017,1,5))
        self.instance.enqueue_command(command)

        startLength = len(self.instance.commandQueue)
        self.instance.delete_command(0)
        endLength = len(self.instance.commandQueue)

        self.assertFalse((startLength == endLength), False)

    #delete_command: commandQueue does not contain the deleted command
    def test_que_excludes_command(self):
        self.instance = CommandManager()
        command = ICommand(datetime(2017,1,5))
        self.instance.enqueue_command(command)

        startContains = (command in self.instance.commandQueue)
        self.instance.delete_command(0)
        endContains  = (command in self.instance.commandQueue)

        self.assertFalse(endContains,startContains)

    #create_new_timer: sets a new timer
    def test_sets_new_timer(self):
        self.instance = CommandManager()
        oldTimer = copy.copy(self.instance.myTimer)
        command = ICommand(datetime(2017,1,5))

        self.instance.commandQueue.append(command)
        self.instance.create_new_timer()
        newTimer = copy.copy(self.instance.myTimer)

        self.assertFalse((oldTimer == newTimer),False)

    #execute_command: Head is not the same after execute has been run
    def test_head_is_not_same(self):
        self.instance = CommandManager()

        command = ICommand(datetime(2017,1,5))
        command2 = ICommand(datetime(2018,1,5))
        self.instance.enqueue_command(command)
        self.instance.enqueue_command(command2)

        oldHead = (self.instance.commandQueue[:])[0]
        self.instance.execute_command()
        startHead = (self.instance.commandQueue[:])[0]
        self.assertTrue((oldHead != startHead),True)

    #execute_command: myTimer is updated after execute has been run
    def test_myTimer_is_updated(self):
        self.instance = CommandManager()

        command = ICommand(datetime(2017,1,5))
        command2 = ICommand(datetime(2018,1,5))
        self.instance.enqueue_command(command)
        self.instance.enqueue_command(command2)

        startTimer = copy.copy(self.instance.myTimer)
        self.instance.execute_command()
        endTimer = copy.copy(self.instance.myTimer)

        self.assertTrue((startTimer != endTimer),True)

    #main_loop: if there is something in the que it should be executed
    def test_is_head_executed(self):
        self.instance = CommandManager()

        command = ICommand(datetime(2017,1,5))
        self.instance.enqueue_command(command)
        head = copy.copy(self.instance.commandQueue[0])
        self.instance.main_loop()
        try:
            self.instance.commandQueue[0]
            self.fail("head is not executed")
        except IndexError:
            self.assertTrue(True,True)

    #main_loop: if commandQueue.length == 0 nothing should happen
    def test_empty_queue_behaviour(self):
        self.instance = CommandManager()
        startQue = copy.copy(self.instance.commandQueue)
        self.instance.main_loop()
        endQue = copy.copy(self.instance.commandQueue)
        self.assertTrue((startQue == endQue), True)

    #main_loop: if commandQueue.length > 1 the  timer should be updated
    def test_is_myTimer_updated(self):
        self.instance = CommandManager()

        command = ICommand(datetime(2017,1,5))
        command2 = ICommand(datetime(2018,1,5))
        self.instance.enqueue_command(command)
        self.instance.enqueue_command(command2)

        startTimer = copy.copy(self.instance.myTimer)
        self.instance.main_loop
        endTimer = copy.copy(self.instance.myTimer)

        self.assertTrue((startTimer != endTimer), True)

    #main_loop: if commandQueue.length == 1 the timer should not be updated
    def test_myTimer_is_not_updated(self):
        self.instance = CommandManager()

        command = ICommand(datetime(2017,1,5))
        self.instance.enqueue_command(command)

        startTimer = self.instance.myTimer
        self.instance.main_loop()
        endTimer = self.instance.myTimer

        self.assertTrue((startTimer == endTimer), True)

if __name__ == "__main__":
    ut.main()
