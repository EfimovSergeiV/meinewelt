from rest_framework import serializers
from blog.models import *


class TechSerializer(serializers.ModelSerializer):
    """ -*- """
    
    class Meta:
        model = TechModel
        fields = ('id', 'name', 'skill' )