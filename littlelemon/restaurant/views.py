from django.http import response # type: ignore
from django.shortcuts import render # type: ignore

from rest_framework import generics # type: ignore
from rest_framework import permissions, viewsets # type: ignore
from rest_framework.decorators import api_view, permission_classes # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore

from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
# class MenuItemsView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

#@api_view()
#@permission_classes([IsAuthenticated])
#@authentication_classes([TokenAuthentication])
#def msg(request):
#    return response({"message":"This view is protected"})
