from django.conf import settings
from django.db import models
from db.models import TimeStampedModel

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
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
    )

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)


class Comment(TimeStampedModel):

    message = models.TextField()
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
    )
    image = models.ForeignKey(
        Images,
        null=True,
    )


class Like(TimeStampedModel):

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
    )
    image = models.ForeignKey(
        Images,
        null=True,
    )