## Commands cheatsheet
Running a local testserver
- Navigate to the folder containing the "manage.py" file. Then type:
```
python manage.py runserver
```

Running a test suite
- Navigate to the folder containing the "maketest" file. Then type:
```
make -f maketest [unit | acceptance | integration]
```

# Projects-in-Stock
Københavns Universitet - Datalogisk Institut - Softwareudvikling - Projects-in-Stock

Mads, Herluf & Philip  

## General
Compiler: **Python 2.7**

The following modules are dependencies of the project and will need to be installed.
- `Django`: Framework for creating webapplications
- `Requests`: A module for requesting HTTP responses
- `Robot`: Framework for acceptancetesting
- `Selenium2Libary`: Browser automation for acceptancetesting

The following commands will install all dependencies needed to execute run the website plus running the testsuite:
```
$ pip install django
$ pip install requests
$ pip install robotframework
$ pip install robotframework-selenium2library
```

## virtualenv setup
It is strongly recommended to place the project inside a virtual enviornment with the appropriate dependencies installed. 
A virtual enviornment can be created using the python module `virtualenv`. A fully configured virtual enviornment can be created in the current directory with the following commands:
```
virtualenv [ENV_NAME] -p python2.7
cd [ENV_NAME]
source bin/activate
$ pip install django
$ pip install requests
$ pip install robotframework
$ pip install robotframework-selenium2library
```

## Running tests
The projects different testsuites can be run using the makefile *maketest* which is located in the *Product* folder. The syntax is:
```
make -f maketest [THE_TESTING_SUITE_TO_RUN]
```

There are three different suites:
- `unit`: Unittesting of the modules *Scraper*, *CommandManager* and their subclasses.
- `integration`: Integrationtesting of the adapter between the webapp and the other modules.
- `acceptance`: Automated acceptancetesting using the robot framework. 
  - **NB.** A local testserver must be active in *another* terminal window. 

