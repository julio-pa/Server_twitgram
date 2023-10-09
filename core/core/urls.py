from django.urls import include, path, re_path
from django.contrib import admin
from django.views.generic import TemplateView

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/tweet/', include('apps.server.urls')),
    path('api/user/', include('apps.user.urls')),
    path('api/media/', include('apps.media_upload.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]
