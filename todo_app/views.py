from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_app.forms import TaskUpdateForm, TaskCreateForm
from todo_app.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tags-list")


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("task-list")


class TaskDeleteView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("task-list")


