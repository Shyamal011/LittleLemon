from django.http import response
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
#from rest_framework.decorators import api_view, permission_classes, authentication_classes
#from rest_framework.authentication import TokenAuthentication
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.

# Index view for rendering the homepage
def index(request):
    return render(request, 'index.html', {})

# View for listing and creating menu items
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# View for retrieving, updating, and deleting a single menu item
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]  # Ensure authentication for update and delete

# ViewSet for Booking with authentication check
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # Ensure authentication for all booking actions

class CustomLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get the token associated with the current user
            token = Token.objects.get(user=request.user)
            # Delete the token to log the user out
            token.delete()
            return Response({"message": "Logged out successfully"}, status=200)
        except Token.DoesNotExist:
            return Response({"message": "No active token found"}, status=400)

# Uncomment and use this view for a protected message endpoint
#@api_view()
#@permission_classes([IsAuthenticated])
#@authentication_classes([TokenAuthentication])
#def msg(request):
#    return response({"message": "This view is protected"})
