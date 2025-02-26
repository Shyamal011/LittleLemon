from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="IceCream", 
            price=80, 
            inventory=100
        )

# Compare the string representation of the new menu item with the expected string
        expected_representation = f'{item.title}: {item.price}'  # "IceCream: 80" without extra spaces
        self.assertEqual(str(item), expected_representation)
