from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from sistema.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('veiculos/', include('veiculo.urls'), name='veiculo')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

