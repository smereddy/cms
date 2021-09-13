from django.urls import path
from . import views
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
    VehiclesListView,
    VehiclesUpdateView,
    VehiclesDeleteView,
    VehiclesCreateView,
)

urlpatterns = [

    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('<int:pk>/comment/edit/',
         CommentUpdateView.as_view(), name='comment_edit'),
    path('<int:pk>/comment/delete/',
         CommentDeleteView.as_view(), name='comment_delete'),
    path('<int:client_id>/comment/create/',
         CommentCreateView.as_view(), name='comment_create'),
    path('<int:pk>/vehicle/edit/',
         VehiclesUpdateView.as_view(), name='vehicles_edit'),
    path('<int:pk>/vehicle/delete/',
         VehiclesDeleteView.as_view(), name='vehicles_delete'),
    path('<int:client_id>/vehicle/create/',
         VehiclesCreateView.as_view(), name='vehicles_create'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('vehicles/', VehiclesListView.as_view(), name='vehicles_list'),
    path('', ClientListView.as_view(), name='client_list'),

]
