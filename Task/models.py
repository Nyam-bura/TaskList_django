from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


COUNTY_CHOICES = (
    ("uasin_gishu", "Uasin Gishu"),
    ("samburu", "Samburu"),
    ("meru", "Meru"),
    ("kajiado", "Kajiado"),
    ("embu", "Embu"),
    ("kiambu", "Kiambu"),
    ("kilifi", "Kilifi"),
)
ID_DOCUMENT = (("passport", "Passport"), ("id_number", "id number"))
STATUS_CHOICE = (
    ("Open", "open"),
    ("pending", "Pending"),
    ("inprogress", "Inprogress"),
    ("complete", "Complete"),
    ("inreview", "Inreview"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
    ("blocked", "Blocked"),
    ("closed", "Closed"),
)


class UserManager(BaseUserManager):
    """Customizing default user model to override some creation features"""

    def create_user(
        self,
        username,
        email,
        phone_number,
        county,
        id_number,
        id_document_type,
        password=None,
    ):
        if username is None:
            raise TypeError("Users should have a username")
        if email is None:
            raise TypeError("Users should have a email")
        if county is None:
            raise TypeError("Users should have a county")
        if id_number is None:
            raise TypeError("Users should have an id_number")
        if phone_number is None:
            raise TypeError("Users should have a phone")
        if id_document_type is None:
            raise TypeError("Users should have an id_document_type")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone_number=phone_number,
            county=county,
            id_number=id_number,
            id_document_type=id_document_type,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if username is None:
            raise TypeError("Users should have a username")
        if password is None:
            raise TypeError("Users should have a password")
        if email is None:
            raise TypeError("Users should have a email")
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    password = models.CharField(("password"), max_length=128)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    phone_number = models.CharField(max_length=13, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    if_superuser = models.BooleanField(default=False)
    county = models.CharField(max_length=256, choices=COUNTY_CHOICES, null=True)
    id_number = models.CharField(max_length=50, null=True)
    id_document_type = models.CharField(max_length=50, choices=ID_DOCUMENT, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()


class DataModel(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assigned"
    )
    assigned_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assignee"
    )
    creation_date = models.DateField(auto_now=False)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICE)


class Meta:
    abstract = True


class Task(DataModel):
    class Meta:
        ordering = ["creation_date"]


class SubTask(DataModel):
    data_task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="data", default=True
    )

    class Meta:
        ordering = ["due_date"]

    # metadata = models.JSONField()


class Attribute(models.Model):
    task_name = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="_assigned"
    )
