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


class BoardComment(models.Model):
    class Meta(object):
        db_table = 'board_comment'

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
