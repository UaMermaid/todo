from django.shortcuts import render
from django.views import generic

from todo_app.models import Tag


class TagListView(generic.ListView):
    model = Tag

