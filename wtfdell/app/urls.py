from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.index2, name='detail'),
    path('add', views.addNewTodo, name='add'),
    path('complete/<int:pk>', views.completeTodo, name='complete'),
    path('delete/<int:pk>', views.deleteTodo, name='delete'),
    path('update/<int:pk>', views.updateTodo, name='update'),
]
