from django.db import models
from config.utility.BaseModel import BaseModel


class Board(BaseModel):
    class Meta(object):
        db_table = 'board'

    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
