from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('singup/', views.singup, name='singup'),
    path('table/',views.table,name='table'),
    path('newuser/',views.newuser,name='newuser'),
<<<<<<< HEAD

=======
>>>>>>> 9ceb6f472701d3a896130553b698ca7f574ec932
]
