from django.urls.conf import path
from .views import inicio

# URLs de las views de la AppKiosko

urlpatterns = [
    path('', inicio, name='vista_inicio')
]
