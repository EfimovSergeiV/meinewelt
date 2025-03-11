from django.urls import path, re_path
from mw.views import ProjectView


urlpatterns = [
    path('projects/<slug:status>/', ProjectView.as_view(), name='projects'),
]
