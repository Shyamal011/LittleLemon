from django.http import response
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer

# Create your views here.

# Index view for rendering the homepage
def index(request):
    return render(request, 'index.html', {})

# View for listing and creating menu items
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

# View for retrieving, updating, and deleting a single menu item
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]  # Ensure authentication for update and delete

# ViewSet for Booking with authentication check
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # Ensure authentication for all booking actions

# Uncomment and use this view for a protected message endpoint
@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    return response({"message": "This view is protected"})
