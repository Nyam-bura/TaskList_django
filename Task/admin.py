# from typing import Self
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from Task.models import SubTask, Attribute, User, Task

User = get_user_model()


class UserAdmin(UserAdmin):
    model = User
    list_display = [
        "username",
        "phone_number",
        "county",
        "id_number",
        "id_document_type",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("phone_number", "county", "id_number", "id_document_type")}),)


admin.site.register(User, UserAdmin)


class SubTaskAdmin(admin.ModelAdmin):
    model = SubTask
    list_display = ['task_name','description','assigned_to','assigned_by','creation_date','due_date','status']

admin.site.register(SubTask, SubTaskAdmin)


class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ['task_name','description','assigned_to','assigned_by','creation_date','due_date','status']
admin.site.register(Task, TaskAdmin)

class AttributeAdmin(admin.ModelAdmin):
    model = Attribute
    list_display = ['task_name','assigned_to']

admin.site.register(Attribute,AttributeAdmin)







































# class DataModelAdmin(admin.ModelAdmin):
#     model=DataModel
#     jsonfield = ['description','due_date','creation_date','assigned_to','assigned_by','task']

# admin.site.register(DataModel, DataModelAdmin)

# class DataModelAdmin(admin.ModelAdmin):
# model=DataModel
# jsonfield = [   'task_name','description','title','creation_date','due_date','completed']
# list_display = ['task_name','description','assigned_to','assigned_by','creation_date','due_date','completed_status']

# admin.site.register(DataModel,DataModelAdmin)