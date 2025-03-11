from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from mw.models import ProjectModel
from mw.serializers import ProjectsSerializer


class ProjectView(APIView):
    """ Проекты """

    def get(self, request, status):

        projects_qs = ProjectModel.objects.filter(status=status)
        serializer = ProjectsSerializer(projects_qs, many=True, context={'request': request})

        return Response(serializer.data)
