from rest_framework import generics , mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or title  
        serializer.save(content=content)
        # send a django signal
        
        
product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIview(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'pk'

product_detail_view = ProductDetailAPIview.as_view()

class ProductUpdateAPIview(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content :
            instance.content = instance.title

product_update_view = ProductUpdateAPIview.as_view()
   
class ProductDestroyAPIview(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIview.as_view()
   

# class ProductListAPIview(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
 
    
# product_list_view = ProductListAPIview.as_view()


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs): #HTTP -> post
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    # def post() #HTTP -> post
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or title  
        if content is None:
            content = "Chi tiet ve khoa hoc"
        serializer.save(content = content)
        
        
        
product_mixin_view = ProductMixinView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request,pk = None, *args, **kwargs):
    method = request.method 
    
    if method == "GET":
        if pk is not None:
            # detail view
            obj =  get_object_or_404(Product , pk = pk) # Http404
            data = ProductSerializer(obj, many = False).data  
            return Response(data)
        
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)
        
    if method == "POST":
        # create an item
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
           # instance = serializer.save()
           # instance = form.save()
           print(serializer.data)
        return Response({"invalid":"not good data"}, status=400)
    
            
        