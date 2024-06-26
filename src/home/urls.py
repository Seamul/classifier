from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.HelloWorld.as_view(), name='hello_world'),
    path('title_classification/', views.TitleClassificationView.as_view(), name='title_classification'),
    
]