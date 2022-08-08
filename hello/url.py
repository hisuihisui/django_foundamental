from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next', views.next, name='next'),
    # path('', views.index_before, name='index_before'),
    # path('<int:id>/<nickname>/', views.index, name='index'),
]
