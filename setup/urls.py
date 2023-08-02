from django.contrib import admin
from django.urls import path, include
from miles.views import DepoimentosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet, basename='Depoimentos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
