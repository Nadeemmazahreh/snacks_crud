from snacks.models import Snack
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    UpdateView, 
    DeleteView,
    CreateView,
    
)

# Create your views here.
class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    # context_object_name = 'snacks'

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack
    # context_object_name = 'snacks'

class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["name", "description", "purchaser"]
    success_url = reverse_lazy("snack_list")


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["name", "description", "purchaser"]
    success_url = '/'


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")
