# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from .models import Board
from .forms import RegisterForm, CommentForm


class List(ListView):
    model = Board
    # paginate_by = 5
    template_name = 'board/list.html'


class Detail(ModelFormMixin, DetailView):
    model = Board
    form_class = CommentForm
    template_name = 'board/detail.html'

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        comment = form.save(commit=False)
        comment.board_id = get_object_or_404(Board, pk=post_pk)
        comment.created_at = timezone.now()
        comment.save()
        return redirect('board:detail', pk=post_pk)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.object = self.get_object()
            return self.form_invalid(form)


class Create(CreateView):
    model = Board
    template_name = 'board/create.html'
    form_class = RegisterForm
    success_url = '/board/list'

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' バリデーションに失敗した時 '''
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)


class Update(UpdateView):
    model = Board
    template_name = 'board/update.html'
    form_class = RegisterForm
    success_url = '/board/list'

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' バリデーションに失敗した時 '''
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)
