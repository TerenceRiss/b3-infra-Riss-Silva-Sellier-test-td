import unittest
from product import Product
from cart import Cart
from order import Order

class TestOrderDiscount(unittest.TestCase):
    def setUp(self):
        """Initialiser les données pour les tests."""
        self.product1 = Product("Laptop", 1000.0, 5)
        self.product2 = Product("Headphones", 200.0, 10)
        self.cart = Cart()
        self.cart.add_product(self.product1, 1)  # Ajoute 1 Laptop au panier
        self.cart.add_product(self.product2, 2)  # Ajoute 2 Headphones au panier

    def test_discount_applied_correctly(self):
        """Test de la remise avec un pourcentage valide."""
        order = Order(self.cart, discount_percentage=10)  # 10% de remise
        self.assertAlmostEqual(order.total, 1260.0)  # 1000 + (200*2) - 10%

    def test_no_discount(self):
        """Test sans remise."""
        order = Order(self.cart, discount_percentage=0)  # 0% de remise
        self.assertAlmostEqual(order.total, 1400.0)  # Total sans remise

    def test_full_discount(self):
        """Test avec une remise de 100%."""
        order = Order(self.cart, discount_percentage=100)  # 100% de remise
        self.assertAlmostEqual(order.total, 0.0)  # Total doit être 0€

    def test_negative_discount(self):
        """Test avec une remise négative."""
        with self.assertRaises(ValueError):
            Order(self.cart, discount_percentage=-10)  # Remise négative

    def test_over_100_percent_discount(self):
        """Test avec une remise de plus de 100%."""
        with self.assertRaises(ValueError):
            Order(self.cart, discount_percentage=110)  # Remise > 100%

    def test_empty_cart(self):
        """Test avec un panier vide."""
        empty_cart = Cart()
        with self.assertRaises(ValueError):
            Order(empty_cart, discount_percentage=10)  # Panier vide

if __name__ == '__main__':
    unittest.main()
