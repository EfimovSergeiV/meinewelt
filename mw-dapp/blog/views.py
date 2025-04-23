from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from blog.models import *
from blog.serializers import *

class TechView(APIView):
    """ -*- """

    def get(self, request):
        """ GET """

        qs = TechModel.objects.filter(activated=True)
        sr = TechSerializer(qs, many=True, context={ 'request': request })
        print(sr.data)
        return Response(sr.data)