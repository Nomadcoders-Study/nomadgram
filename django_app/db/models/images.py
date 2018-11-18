from django.conf import settings
from django.db import models

from db.models import TimeStampedModel, User

__all__ = (
    'Images',
    'Comment',
    'Like',
)


class Images(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(
        max_length=140,
    )
    caption = models.TextField()


class Comment(TimeStampedModel):

    message = models.TextField()


class Like(TimeStampedModel):

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )