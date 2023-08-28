from . import views
from django.contrib import admin
from django.urls import path
urlpatterns = [
        path('admin/', admin.site.urls),
        path('',views.register,name='register'),
        path('elogin/',views.elogin, name='login'),
        path('dashbord/',views.dashbord, name='dashbord'),
        path('Coupens/',views.Coupens, name='Coupens'),
        path('filtered_data/',views.filtered_data, name='filtered_data'),
        ]

