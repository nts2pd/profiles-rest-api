from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """returns list of apiview features"""

        an_apiview = [
        'uses https methods as function (get, post, patch, put, delete)',
        'is similar to a traditional django view',
        'gives you the most control over your application logic',
        'is mapped manually to urls',
        ]

        return Response({'message': 'howdy', 'an_apiview': an_apiview})
