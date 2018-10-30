# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Board


class ListView(ListView):
    model = Board
    paginate_by = 5
    template_name = 'board/list.html'


class DetailView(DetailView):
    model = Board
    template_name = 'board/detail.html'
