from django.db import models

# Create your models here

#Model used for storing projects
class Project(models.Model):
    title = models.CharField(max_length = 120) #120 is up for discussion
    description = models.TextField()
    #counselors = models.pk
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    degree_choices = (('BSc','Bachelor'),('MS','Masters'))
    degree = models.CharField(max_length = 5, choices = degree_choices,default='BSc')
    topic = models.CharField(max_length = 120) #120 is up for discussion
