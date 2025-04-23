from django.urls import path
from blog.views import *


urlpatterns = [
    path('skills/', TechView.as_view(), name='skils')
]
