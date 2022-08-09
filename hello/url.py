from django.urls import path

from . import views
from .views import HelloView

urlpatterns = [
    path(r'', HelloView.as_view(), name='index'),
    # path('', views.index, name='index'),
    path('next', views.next, name='next'),
    path('form', views.form, name='form'),
    # path('', views.index_before, name='index_before'),
    # path('<int:id>/<nickname>/', views.index, name='index'),
]
