from django.urls import path
from django.http import HttpResponse
from .views import *

urlpatterns = [
    path('', view_home, name='home'),
    path('create-cafe/', view_create_cafe, name='create-cafe'),
    path('cafe-detail/<int:pk>/', view_detail_cafe, name='cafe-detail'),
    path('delete-cafe/<int:pk>/', view_delete_cafe, name='delete-cafe'),
    path('update-cafe/<int:pk>/', view_update_cafe, name='update-cafe'),
]
