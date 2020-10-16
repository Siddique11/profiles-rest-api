from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View """

    def get(self, request, format=None):
        """Returns a list of a APIView feature"""

        an_apiview = ['User HTTP methods as function(get, post, patch, put, delete)',
                      'Is similar to a traditional Django View',
                      'Giver you the most control over your application logic',
                      'Is mapped manually to URLs']

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
