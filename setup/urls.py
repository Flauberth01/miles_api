from django.contrib import admin
from django.urls import path
from miles.views import depoimentos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('depoimentos/', depoimentos),
]
