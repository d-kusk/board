from django.db import models
from django.utils import timezone

from .Board import Board


class BoardComment(models.Model):
    class Meta(object):
        db_table = 'board_comment'

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
