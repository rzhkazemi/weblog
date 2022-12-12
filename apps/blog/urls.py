from django.urls import path

from apps.blog.views import index
app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
]
