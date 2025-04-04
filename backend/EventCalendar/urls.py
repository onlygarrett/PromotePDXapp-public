from django.urls import path
from EventCalendar import views

urlpatterns = [
    path('events/', views.events, name='events-list'),
    path('venues/', views.venues, name='venues-list'),
]
