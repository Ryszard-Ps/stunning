# from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Restaurant


class RestaurantList(ListView):
    model = Restaurant


class RestaurantDetail(DetailView):
    model = Restaurant


class RestaurantCreation(CreateView):
    model = Restaurant
    success_url = reverse_lazy('restaurants:list')
    fields = ['name', 'rating', 'phone', 'city']


class RestaurantUpdate(UpdateView):
    model = Restaurant
    success_url = reverse_lazy('restaurants:list')
    fields = ['name', 'rating', 'phone', 'city']


class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('restaurants:list')
