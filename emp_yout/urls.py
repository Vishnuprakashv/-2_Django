from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('addemp/',views.Addemp),
    path("del-emp/<int:id>",views.delete_emp),
    path("update-emp/<int:id>",views.update_emp),
    path("do-update-emp/<int:id>", views.do_update_employee),
    path("disp/",views.disp)
]
