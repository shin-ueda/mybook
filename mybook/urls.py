from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('cms/', include('cms.urls')),
    path('admin/', admin.site.urls),
]
