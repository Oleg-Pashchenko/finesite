from django.contrib.auth.models import AbstractUser
from django.db import models


class FineUser(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    telegram_chat_id = models.BigIntegerField(null=True, default=None)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'fine_users'
