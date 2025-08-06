from rest_framework.decorators import api_view
from rest_framework.response import Response

from .metrics import REQUEST_COUNTER


@api_view(['GET'])
def hello_world(request):
    try:
        response = Response({"message": "Hello, World!"})
        
        REQUEST_COUNTER.labels(
            endpoint='/hello', 
            method='GET',
            status_code=response.status_code
        ).inc()
        
        return response
        
    except Exception:
        REQUEST_COUNTER.labels(
            endpoint='/hello',
            method='GET',
            status_code=500
        ).inc()
        raise
