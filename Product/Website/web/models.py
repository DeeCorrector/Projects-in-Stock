from django.db import models

#Model used for storing projects
class Project(models.Model):
    title = models.CharField(max_length = 120) #120 is up for discussion
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    degreeChoices = (('BSc','Bachelor'),('MS','Masters'))
    degree = models.CharField(max_length = 5, choices = degreeChoices, default='BSc')
    topic = models.CharField(max_length = 120) #120 is up for discussion

    def __str__(self):
        return self.title

class Counselor(models.Model):
    readonly_fields=('account_id',)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    studyArea = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    projects = models.ManyToManyField(Project)
    url = models.URLField(default="NOURL")
    accountId = models.IntegerField(default=-1)
    statusChoices = (('Available','Available'),('Unavailable','Unavailable'))
    status = models.CharField(max_length=50, choices=statusChoices, default='Available')


    def __str__(self):
        return self.name

    def is_registered(self):
        return not self.accountId == -1
