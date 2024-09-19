from django.contrib import admin
from django.urls import path

from sistema.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('veiculos/', Veiculos.as_view(), name='veiculos')
]

