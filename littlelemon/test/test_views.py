from django.test import TestCase
from restaurant.models import Menu

class MenuItemsViews(TestCase):
    def setUp(self):
        shakshuka = Menu.objects.create(dish='shakshuka', price=8.50, inventory=10)
        Hummus = Menu.objects.create(dish='Hummus', price=5.00, inventory=20)
    
    def test_menu_items_list(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'shakshuka')
        self.assertContains(response, 'Hummus')

    def test_getall(self):
        # URL to access the Menu API (assuming the URL pattern is named 'menu-list')
        url = reverse('menu-list')  # Change 'menu-list' to match your URL name
        response = self.client.get(url)
