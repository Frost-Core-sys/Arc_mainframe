from django.contrib import admin
from django.urls import path, include
from registry_app.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls), # Hooks up all Django Ninja endpoints under /api/
    path('', include('registry_app.urls')), # Points root url to the UI pages
]
