from django.db import models

import datetime
from django.utils.timezone import now
from extended_choices import AutoChoices
from django.contrib.auth.models import AbstractBaseUser

class TODO(models.Model):
    description = models.TextField(default="")
    due_date = models.DateTimeField(default=now)
    STATE = AutoChoices("TODO", "IN_PROGRESS", "Done")
    state = models.CharField(
        null=False, max_length=11, choices=STATE.choices, default=STATE.TODO
    )
