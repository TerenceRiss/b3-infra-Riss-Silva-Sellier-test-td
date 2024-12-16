import unittest
from cart import Cart
from product import Product

class TestCart(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test."""
        self.cart = Cart()
        self.product1 = Product("Laptop", 1200.0, 5)
        self.product2 = Product("Mouse", 25.0, 10)

    def test_get_total_items_empty_cart(self):
        """Test de get_total_items avec un panier vide."""
        self.assertEqual(self.cart.get_total_items(), 0, "Cart should have 0 items when empty")

    def test_get_total_items_with_products(self):
        """Test de get_total_items après avoir ajouté des produits."""
        self.cart.add_product(self.product1, 2)  # Ajoute 2 laptops
        self.cart.add_product(self.product2, 3)  # Ajoute 3 souris
        self.assertEqual(self.cart.get_total_items(), 5, "Cart should correctly sum product quantities")

    def test_get_total_items_after_removal(self):
        """Test de get_total_items après avoir supprimé un produit."""
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product2, 3)
        self.cart.remove_product(self.product1)  # Supprime le laptop
        self.assertEqual(self.cart.get_total_items(), 3, "Cart should update total items after product removal")

    def test_add_zero_quantity(self):
        """Test du cas limite d'ajout d'une quantité de 0."""
        self.cart.add_product(self.product1, 0)
        self.assertEqual(self.cart.get_total_items(), 0, "Adding zero quantity should not affect the cart")

    def test_get_total_items_with_duplicates(self):
        """Test de get_total_items en ajoutant deux fois le même produit."""
        self.cart.add_product(self.product1, 1)
        self.cart.add_product(self.product1, 2)  # Ajoute à nouveau 2 laptops
        self.assertEqual(self.cart.get_total_items(), 3, "Cart should correctly sum quantities for duplicate products")

if __name__ == "__main__":
    unittest.main()