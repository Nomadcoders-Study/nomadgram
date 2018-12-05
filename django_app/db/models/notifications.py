from django.conf import settings
from django.db import models

from db.models import Image
from util import Constant


class Notification(models.Model):

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='creator'
    )
    to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='to'
    )
    notification_type = models.CharField(
        max_length=20,
        choices=Constant.TYPE_CHOICES,
    )
    image = models.ForeignKey(
        Image,
    )
