from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.api_home), # localhost
    # path('products/', include('products.urls'))
    
]

