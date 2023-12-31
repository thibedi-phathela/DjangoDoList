from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('done/<str:pk>', views.done, name='done'),
    path('manage/<int:pk>', views.manage, name='manage')
]
