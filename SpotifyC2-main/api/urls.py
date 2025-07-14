from django.urls import path, include, re_path
from rest_framework import routers
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

router = routers.DefaultRouter()
router.register(r'songs', views.SongViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Spotify API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]