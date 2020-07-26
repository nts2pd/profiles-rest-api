from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns list of apiview features"""

        an_apiview = [
        'uses https methods as function (get, post, patch, put, delete)',
        'is similar to a traditional django view',
        'gives you the most control over your application logic',
        'is mapped manually to urls',
        ]

        return Response({'message': 'howdy', 'an_apiview': an_apiview})

    def post(self, request):
        """create hello message with name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'howdy {}'.format(name)
            return Response({'message': message})

        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ handle a partial update of an object """

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ delete object """
        return Response({'method': 'DELETE'})
