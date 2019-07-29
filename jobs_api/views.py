from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from jobs_api.models import Job
from jobs_api.serializers import JobSerializer
from rest_framework import generics
from rest_framework import permissions


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'retrieve' or self.action == 'create' or self.action == \
                'partial_update' or self.action == 'update':
            permission_classes = [permissions.IsAuthenticated]

        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]

        elif self.action == 'list':
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]


class LoggedInUserJobList(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.filter(stylist=self.request.user)

