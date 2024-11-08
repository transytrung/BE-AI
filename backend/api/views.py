from django.forms.models import model_to_dict
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    View API DRF
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # instance = serializer.save()
        print(serializer.data)    
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
