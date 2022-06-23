from django.urls import path
from . import views

urlpatterns = [
    path('api/animals', views.AnimalList.as_view(), name='animal_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/animals/<int:pk>', views.AnimalDetail.as_view(), name='animal_detail'), # api/contacts will be routed to the ContactDetail view for handling
]