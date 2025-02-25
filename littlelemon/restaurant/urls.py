from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Index route - Function-based view for the homepage or landing page
    path('', views.index, name='index'),  # Home page or index view

    # Menu routes - Class-based views for menu items
    path('menu/', views.MenuItemView.as_view(), name='menu_list'),  # List all menu items
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu_item_detail'),  # Get details of a single menu item

    # Token authentication route
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token authentication endpoint
]
