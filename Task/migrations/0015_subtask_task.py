# Generated by Django 4.2 on 2023-05-12 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0014_rename_name_attribute_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='_task', to='Task.task'),
        ),
    ]