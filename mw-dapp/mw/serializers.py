from rest_framework import serializers
from mw.models import *


class ProjectsSerializer(serializers.ModelSerializer):
    """ Сериализатор широких баннеров """

    class Meta:
        model = ProjectModel
        fields = ('id', 'name', 'url', 'created') 