from django.urls import path, include
from .serializers import AcumuladoDiarioSerializer
from .viewsets import AcumuladoDiarioViewSet
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cases', AcumuladoDiarioViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
