# Generated by Django 4.2 on 2023-04-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0007_alter_task_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=True),
        ),
    ]