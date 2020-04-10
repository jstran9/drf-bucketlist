
from django.db import models
from django.utils import timezone


class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True, default="Title")
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)