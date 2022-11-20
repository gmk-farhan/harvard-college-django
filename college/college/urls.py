from django.contrib import admin
from django.urls import path, include

# passes the control over to groups app
urlpatterns = [
    path('groups/', include('groups.urls')),
    path('admin/', admin.site.urls),
]
