from django.urls import path
from .views import import_qualifyr, import_metadata,dashboard

urlpatterns = [
    path('import_qualifyr/', import_qualifyr, name='import_qualifyr'),
    path('dashboard/', dashboard, name='dashboard'),
    path('import_metadata/', import_metadata, name='import_metadata'),
]