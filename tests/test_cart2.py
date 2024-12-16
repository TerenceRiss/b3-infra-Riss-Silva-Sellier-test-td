import unittest
from cart import Cart
from product import Product

class TestCart(unittest.TestCase):

    def test_cart_is_empty_initially(self):
        cart = Cart()
        self.assertTrue(cart.is_empty())  # Vérifie que le panier est vide

    def test_cart_is_not_empty_after_adding_product(self):
        cart = Cart()
        p1 = Product("Laptop", 1200.0, 5)
        cart.add_product(p1, 1)
        self.assertFalse(cart.is_empty())  # Vérifie que le panier n'est pas vide après ajout

    def test_cart_is_empty_after_removing_product(self):
        cart = Cart()
        p1 = Product("Laptop", 1200.0, 5)
        cart.add_product(p1, 1)
        cart.remove_product(p1)
        self.assertTrue(cart.is_empty())  # Vérifie que le panier est vide après suppression

if __name__ == '__main__':
    unittest.main()
