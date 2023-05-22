# from asyncio import tasks
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
# from Task.admin import SubTaskAdmin

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


class DataModel(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    title= models.CharField(max_length=256)
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
        

#     task = models.ForeignKey(User,on_delete=models.CASCADE,related_name="task")
#     jsonfield =jsonfield()

# def __str__(self):
#     return self.task     
# DataModel.objects.create(description='Creating Models',json={'id':1})
# DataModel.objects.create(task='Task_list',description='Create class',json={'id':{1,2}})

# var_1 = DataModel.objects.filter(json__exact={'id':1})
# var_2 = DataModel.objects.get(json__exact={'id':{1,2}})



