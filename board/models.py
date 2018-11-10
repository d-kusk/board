from django.db import models
from django.utils import timezone


class Board(models.Model):
    class Meta(object):
        db_table = 'board'

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
