from datetime import datetime, timedelta
from threading import Timer
import os


class ICommand():
    def __init__(self, _executionTime):
        self.executionTime = _executionTime

    def execute(self):
        pass

class CommandManager():
    def __init__(self):
        self.commandQueue = []
        self.myTimer = Timer(0,self.main_loop)

    #Creates a new timer an starts it, delay is time until next command
    def create_new_timer(self):
        sleepTime = (self.commandQueue[0].executionTime - datetime.now()).total_seconds()
        self.myTimer = Timer(sleepTime, self.main_loop)
        self.myTimer.start()

    #Executes the first command in the commandQueue and removes it from the queue
    def execute_command(self):
        cmd = self.commandQueue[0]
        cmd.execute()
        self.commandQueue.remove(cmd)

    def main_loop(self):
        if len(self.commandQueue) > 0:
            self.execute_command()
            if len(self.commandQueue) > 0:
                self.create_new_timer()

    #Enqueue a command object
    def enqueue_command(self, newCommand):
        newQueue = self.commandQueue
        for (i,cmd) in enumerate(newQueue):
            if newCommand.executionTime < cmd.executionTime:
                newQueue.insert(i, newCommand)
                #if insert at start
                if i==0:
                    self.myTimer.cancel()
                    self.create_new_timer()
                break
        else:
            newQueue.append(newCommand)
            if not self.myTimer.is_alive():
                self.create_new_timer()
        self.commandQueue = newQueue

    def delete_command(self,cmd_id):
        cmd_to_remove = self.commandQueue[cmd_id]
        self.commandQueue.remove(cmd_to_remove)

class PrintCommand(ICommand):
    def __init__(self, _executionTime, _message):
        super().__init__(_executionTime)
        self.message = _message

    def execute(self):
        print (self.message)

class ShutdownCommand(ICommand):

    def execute(self):
        os.system("shutdown now -h")


if __name__ == "__main__":
    myCommander = CommandManager()
    myCommander.enqueue_command( ShutdownCommand(datetime.now() + timedelta(seconds=15)) )
