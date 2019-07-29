from django.urls import path, include
from rest_framework import routers
from api.views import UserViewSet
from django.conf import settings
from django.conf.urls.static import static
from api.views import StylistAppliedJobsList

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('users/<pk>/applied_jobs', StylistAppliedJobsList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


