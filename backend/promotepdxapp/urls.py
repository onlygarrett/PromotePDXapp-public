from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("EventCalendar.urls")),
    # NOTE: Reactivate this for the worker tasks
    # path('api/', include('UserAccounts.urls')),
]
