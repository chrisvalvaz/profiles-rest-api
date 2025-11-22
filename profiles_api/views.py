from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'It works!!',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
