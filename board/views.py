# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Board, BoardComment
from .forms import RegisterForm, CommentForm


def redirect_to_list(request):
    return HttpResponseRedirect(reverse('list'))


class List(ListView):
    model = Board
    # paginate_by = 5
    template_name = 'board/list.html'


class Detail(ModelFormMixin, DetailView):
    model = Board
    form_class = CommentForm
    template_name = 'board/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.comment(self.kwargs['pk'])
        return context

    def comment(self, board_id):
        return BoardComment.objects.filter(board_id=board_id)

    def form_valid(self, form):
        board_pk = self.kwargs['pk']
        comment = form.save(commit=False)
        comment.board_id = get_object_or_404(Board, pk=board_pk)
        comment.created_at = timezone.now()
        comment.save()
        return redirect('board:detail', pk=board_pk)

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
