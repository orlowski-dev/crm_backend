from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUserModel(AbstractUser):
    email = models.EmailField(
        _('Email address'),
        max_length=126,
        null=False,
        blank=False,
    )
    phone_no = models.CharField(
        _('Phone number'),
        max_length=32,
    )

    # add email to required fields
    REQUIRED_FIELDS = ['email', ]
