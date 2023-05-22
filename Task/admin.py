from msilib.schema import SelfReg
from typing import Self
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import ugettext_lazy as _
from Task.models import SubTask,Attribute,User,DataModel
User = get_user_model()

class UserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'phone_number', 'county','id_number','id_document_type']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('phone_number', 'county','id_number','id_document_type')}),
    )

admin.site.register(User, UserAdmin)

# class TaskAdmin(admin.ModelAdmin):
#     model = Task
#     list_display = []

# admin.site.register(Task,TaskAdmin)
    


class SubTaskAdmin(admin.ModelAdmin):
    model = SubTask
    list_display = ['task','metadata']

admin.site.register(SubTask,SubTaskAdmin)

class DataModelAdmin(admin.ModelAdmin):
    model=DataModel
    jsonfield = ['description','due_date','creation_date','assigned_to','assigned_by','task']

admin.site.register(DataModel, DataModelAdmin)






# Self.register[Combinedtask_subtask] = Combinedtask_subtaskAdmin(Combinedtask_subtask,Self)

class AttributeAdmin(admin.ModelAdmin):
    model = Attribute
    list_display = ['task_name','assigned_to']

admin.site.register(Attribute,AttributeAdmin)

# class Combinedtask_subtaskAdmin(admin.ModelAdmin):
#     model = Combinedtask_subtask
#     list_display = ['description','due_date','creation_date','assigned_to','assigned_by','task']

# admin.site.register(Combinedtask_subtask)

