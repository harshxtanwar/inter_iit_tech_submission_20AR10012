from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('get_query', views.query_searchbar),
    path('post_input', views.post_data)
]