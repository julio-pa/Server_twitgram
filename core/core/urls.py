from django.urls import include, path
from django.contrib import admin


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/tweet/', include('apps.server.urls')),
    path('api/user/', include('apps.user.urls')),
    path('api/media/', include('apps.media_upload.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
