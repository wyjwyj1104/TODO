from django.shortcuts import render
from .models import TODO

class TodosView(generic.ListView):
    model = TODO

    def get_queryset(self):
        return TODO.objects.all()
