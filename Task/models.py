# from .models import SubTask,Task
from django.db import models
from django.contrib.auth.models import AbstractUser



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

# //Creating task and adding a SubTask
# Generating Apis on how to add task and subtask

class User(AbstractUser):
    phone_number = models.CharField(max_length=13)
    county = models.CharField(max_length=256,choices=COUNTY_CHOICES)
    id_number = models.CharField(max_length=100)
    id_document_type=models.CharField(max_length=50,choices=ID_DOCUMENT)

class DataModel(models.Model):
    task_id = models.IntegerField()
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_assigned_to")
    assigned_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_assigned_by",null=True)
    creation_date = models.DateField(auto_now=False)
    due_date = models.DateField(blank=True,null=True)
    completed = models.CharField(max_length=100,choices=STATUS_CHOICE)
    

# class Task(models.Model):
#     class Meta:
#         ordering = ['task']
        
class SubTask(models.Model): 
    task = models.ForeignKey(DataModel,on_delete=models.CASCADE,related_name="task")
    metadata =models.JSONField()


class Attribute(models.Model):
    task_name = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="_assigned")


# class Task(models.Model):
#     class Meta:
#         abstract = True    







class Task(DataModel):
    class Meta:
        ordering = ['due_date']
        
class SubTask(DataModel):
    data_task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name="data",default=True)
    class Meta:
        ordering = ['description']

    # metadata = models.JSONField()
        
   
class Attribute(models.Model):
    task_name = models.CharField(max_length=100)        
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="_assigned")
