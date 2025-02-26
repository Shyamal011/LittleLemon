# test_views.py
from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu

class MenuViewsTest(TestCase):
    def setUp(self):
        # Creating some menu items for testing
        self.menu_item_1 = Menu.objects.create(title="IceCream", price=80, inventory=50)
        self.menu_item_2 = Menu.objects.create(title="Shakshuka", price=150, inventory=20)
        self.menu_item_3 = Menu.objects.create(title="Pizza", price=120, inventory=30)

        # Set up the API client
        self.client = APIClient()
        self.url = '/api/menu/'  # Ensure this matches the correct URL

    def test_menu_items_list(self):
        # Send a GET request to the menu endpoint
        response = self.client.get(self.url)

        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains 'Shakshuka'
        self.assertContains(response, 'Shakshuka')
