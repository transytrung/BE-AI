from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import Program
from .serializers import ProgramSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    View API DRF for Program
    """
    serializer = ProgramSerializer(data=request.data)
    if serializer.is_valid():
        # Optionally save the instance if needed
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
