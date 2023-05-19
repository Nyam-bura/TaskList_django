# from django.db import models
from django.db import models
# from datetime import date
from django.contrib.auth.models import AbstractUser
# from Task.admin import Combinedtask_subtask

# import django
# django.setup()

# from Task.models import Task



COUNTY_CHOICES=(
     ('uasin_gishu','Uasin Gishu'),
     ('samburu','Samburu'),
     ('meru','Meru'),
     ('kajiado','Kajiado'),
     ('embu','Embu')
    )
ID_DOCUMENT=(
    ('passport','Passport'),
    ('id_number','id number')
)
STATUS_CHOICE = (
    ('open','Open'),
    ('pending','Pending'),
    ('inprogress','Inprogress'),
    ('complete','Complete'),
    ('inreview','InReview'),
    ('accepted','Accepted'),
    ('rejected','Rejected'),
    ('blocked','Blocked'),
    ('closed','Closed')
)

class User(AbstractUser):
    phone_number = models.CharField(max_length=13)
    county = models.CharField(max_length=256,choices=COUNTY_CHOICES)
    id_number = models.CharField(max_length=100)
    id_document_type=models.CharField(max_length=50,choices=ID_DOCUMENT)

class Task(models.Model):
    task_subtask = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    title= models.CharField(max_length=256)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_assigned_to")
    assigned_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_assigned_by",null=True)
    creation_date = models.DateField(auto_now=False)
    due_date = models.DateField(blank=True,null=True)
    completed = models.CharField(max_length=100,choices=STATUS_CHOICE)


class SubTask(models.Model):
    task_subtask = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    due_date = models.DateField(blank=True,null=True)
    creation_date = models.ForeignKey(Task,on_delete=models.CASCADE,related_name="_date")
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="_assigned_to")
    assigned_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="_user")
    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name="_task",default=True)

# class Combinedtask_subtask(BaseException):
#     description = models.TextField()
#     due_date = models.DateField(blank=True,null=True)
#     creation_date = models.DateField(auto_now=False)
#     assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="assigned_to")
#     assigned_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="assigned_by")
#     task = models.ForeignKey(on_delete=models.CASCADE, related_name="task")

#     class Meta:
#         abstract = True


# class Task(Combinedtask_subtask):
#     class Meta:
#         pass
#         ordering = ['description']

        


# class SubTask(Combinedtask_subtask):
#     class Meta:
#         pass
#         ordering = ['description']
        



class Attribute(models.Model):
    task_name = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="_assigned")
