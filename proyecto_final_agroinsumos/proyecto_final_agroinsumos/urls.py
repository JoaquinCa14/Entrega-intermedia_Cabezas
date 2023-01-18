from django.contrib import admin
from django.urls import path, include

from proyecto_final_agroinsumos.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),

    path('products/', include ('products.urls')),
    path('orders/', include ('orders.urls')),
    path('providers/', include ('providers.urls')),
]
