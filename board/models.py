from django.db import models
from django.utils import timezone


class Board(models.Model):
    class Meta(object):
        db_table = 'board'

    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
