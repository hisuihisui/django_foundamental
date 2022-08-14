from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    # as_ViewメソッドでViewインスタンスへ変換
    path('list', views.FriendList.as_view()),
    path('detail/<int:pk>', views.FriendDetail.as_view()),
    path('find', views.find, name='find'),
    path('check', views.check, name='check'),
]
