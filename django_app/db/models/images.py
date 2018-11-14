from django.db import models

from db.models import TimeStampedModel

__all__ = (
    'Images',
    'Comment',
)


class Images(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(
        max_length=140,
    )
    caption = models.TextField()


class Comment(TimeStampedModel):

    message = models.TextField()
