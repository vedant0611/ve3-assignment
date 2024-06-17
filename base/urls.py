from django.urls import path
from .views import csvupload

urlpatterns = [
    path('', csvupload, name='csvupload'),
]
