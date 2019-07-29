from django.urls import path, include
from rest_framework import routers
from jobs_api.views import JobViewSet, LoggedInUserJobList

router = routers.DefaultRouter()
router.register('applied_jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('jobs/myjobs', LoggedInUserJobList.as_view())
]
