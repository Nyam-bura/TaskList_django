# Generated by Django 4.2.1 on 2023-06-19 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('creation_date', models.DateField()),
                ('due_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Open', 'open'), ('pending', 'Pending'), ('inprogress', 'Inprogress'), ('complete', 'Complete'), ('inreview', 'Inreview'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('blocked', 'Blocked'), ('closed', 'Closed')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('datamodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Task.datamodel')),
            ],
            options={
                'ordering': ['creation_date'],
            },
            bases=('Task.datamodel',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=13, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('if_superuser', models.BooleanField(default=False)),
                ('county', models.CharField(choices=[('uasin_gishu', 'Uasin Gishu'), ('samburu', 'Samburu'), ('meru', 'Meru'), ('kajiado', 'Kajiado'), ('embu', 'Embu'), ('kiambu', 'Kiambu'), ('kilifi', 'Kilifi')], max_length=256, null=True)),
                ('id_number', models.CharField(max_length=50, null=True)),
                ('id_document_type', models.CharField(choices=[('passport', 'Passport'), ('id_number', 'id number')], max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='datamodel',
            name='assigned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='datamodel',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_assigned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('datamodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Task.datamodel')),
                ('data_task', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='data', to='Task.task')),
            ],
            options={
                'ordering': ['due_date'],
            },
            bases=('Task.datamodel',),
        ),
    ]
