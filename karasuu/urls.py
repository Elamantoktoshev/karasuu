from django.contrib import admin
from django.urls import path, include
from ads.views import Kara

urlpatterns = [
    'api_views',
    path('admin/', admin.site.urls),
    path('ads/', include('ads.urls')),
    path("", Kara)
]
