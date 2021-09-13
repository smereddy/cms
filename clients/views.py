from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Comment, Client, Vehicles
from django.urls import reverse_lazy


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'

    def get_queryset(self):
        objects = Client.objects.filter(author=self.request.user)
        return objects


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ('comment',)
    success_url = reverse_lazy('client_list')
    template_name = 'comments_edit.html'


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comments_delete.html'
    success_url = reverse_lazy('client_list')


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comments_create.html'
    fields = ('comment',)
    success_url = reverse_lazy('client_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.client_id = self.kwargs["client_id"]
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class VehiclesListView(LoginRequiredMixin, ListView):
    model = Vehicles
    template_name = 'vehicles_list.html'


class VehiclesUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicles
    success_url = reverse_lazy('client_list')
    fields = ('make', 'model', 'VIN', 'last_service_date', 'purchase_date',)
    template_name = 'vehicles_edit.html'


class VehiclesDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicles
    template_name = 'vehicles_delete.html'
    success_url = reverse_lazy('client_list')


class VehiclesCreateView(LoginRequiredMixin, CreateView):
    model = Vehicles
    template_name = 'vehicles_create.html'
    success_url = reverse_lazy('client_list')
    fields = ('make', 'model', 'VIN', 'last_service_date', 'purchase_date',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.client_id = self.kwargs["client_id"]
        return super().form_valid(form)
