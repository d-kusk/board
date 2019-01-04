from django.db import models
from config.utility.BaseModel import BaseModel

from .Board import Board


class BoardComment(BaseModel):
    class Meta(object):
        db_table = 'board_comment'

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment
