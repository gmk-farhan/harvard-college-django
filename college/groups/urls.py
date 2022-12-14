from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# here it will be groups/home,  groups/about
urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
