from django.urls import path
from basic_app import views

#TEMPLATE TEGGING

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative_url_template/', views.relative_url_template, name='relative_url_template'),
]