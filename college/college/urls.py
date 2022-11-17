from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/', include('..groups.urls.py')),
    path('admin/', admin.site.urls),
]
