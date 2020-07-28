from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


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

class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ return a hello message"""

        a_viewset = [
        'uses actions (list, create, retrieve, update, partial_update)',
        'automatically maps to urls using routers',
        'provides more functionality with less code',
        ]

        return Response({'message': 'Howdy!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new message"""
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

    def retrieve(self, request, pk=None):
        """handle getting object by id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ update object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handle removing an object"""
        return Response({'http_method': 'DELETE'})
