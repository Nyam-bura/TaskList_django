# Generated by Django 4.2.1 on 2023-06-06 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datamodel',
            old_name='status',
            new_name='completed_status',
        ),
    ]