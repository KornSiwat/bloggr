import sys

from django.db import models
from django.contrib.auth.models import User


class BloggrUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_day = models.DateTimeField('registered_day', auto_now=True)

    def __str__(self):
        return self.user

    class Meta:
        app_label = "authenticationApp"


sys.modules[__name__] = BloggrUser
