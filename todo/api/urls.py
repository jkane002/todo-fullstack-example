from django.urls import paths
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
]
