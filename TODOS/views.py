from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import TODO

class TODOList(ListView):
    model = TODO
    fields = "__all__"

class TODODetail(DetailView):
    model = TODO
    fields = "__all__"

class TODOCreate(CreateView):
    model = TODO
    fields = "__all__"

    def get_success_url(self):
        return reverse("todos_detail", kwargs={'pk' : self.object.pk})

class TODOUpdate(UpdateView):
    model = TODO
    fields = "__all__"
    success_url = reverse_lazy('todos_list')

class TODODelete(DeleteView):
    model = TODO
    success_url = reverse_lazy('todos_list')
