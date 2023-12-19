from django.db import models

from authentification.models import FineUser


class Target(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    from_date = models.DateTimeField(auto_now_add=True, null=False)
    to_date = models.DateTimeField(null=True, default=None)
    is_finished = models.BooleanField(default=False, null=False)
    user_id = models.ForeignKey(FineUser, on_delete=models.DO_NOTHING, null=False)


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=False)
    update_date = models.DateTimeField(auto_now=True, null=False)
    data = models.TextField(null=False, default="")
    user_id = models.ForeignKey(FineUser, on_delete=models.DO_NOTHING, null=False)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=False)
    to_date = models.DateTimeField(null=True, default=None)
    is_finished = models.BooleanField(default=False, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
    text = models.TextField(null=False, default="")
    user_id = models.ForeignKey(FineUser, on_delete=models.DO_NOTHING, null=False)


class Finance(models.Model):
    is_income = models.BooleanField(null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    text = models.TextField(null=False)
    category = models.CharField(max_length=255, null=False)
    date = models.DateTimeField()

    user_id = models.ForeignKey(FineUser, on_delete=models.DO_NOTHING, null=False)
