from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer

class PropertyView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyViewRetriveUpdateDestroyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    

