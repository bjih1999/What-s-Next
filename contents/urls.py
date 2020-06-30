from django.urls import path
from . import views

urlpatterns = [
    # path('', views.content_list, name="content_list"),
    path('load_database', views.load_database, name="load_database")
]