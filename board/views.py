# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages

from .models import Board
from .forms import RegisterForm


class List(ListView):
    model = Board
    # paginate_by = 5
    template_name = 'board/list.html'


class Detail(DetailView):
    model = Board
    template_name = 'board/detail.html'


class Create(CreateView):
    model = Board
    template_name = 'board/add.html'
    form_class = RegisterForm
    success_url = '/board'

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' バリデーションに失敗した時 '''
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)
