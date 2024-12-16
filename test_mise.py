import unittest
from product import Product
from cart import Cart

class TestCartMethods(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test"""
        # Création d'un produit pour les tests
        self.product = Product("Headphones", 100.0, 10)  # 10 unités disponibles
        self.cart = Cart()

    def test_update_quantity_to_zero(self):
        """Test de la mise à jour de la quantité à zéro"""
        # Ajouter le produit au panier
        self.cart.add_product(self.product, 5)
        # Mettre à jour la quantité à zéro (devrait enlever le produit du panier)
        self.cart.update_product_quantity(self.product, 0)
        # Vérifier que le produit a été retiré du panier
        self.assertNotIn(self.product, self.cart.items)

    def test_update_quantity_to_valid_number(self):
        """Test de la mise à jour de la quantité avec une valeur valide"""
        # Ajouter le produit au panier
        self.cart.add_product(self.product, 5)
        # Mettre à jour la quantité à 6 (doit être accepté)
        self.cart.update_product_quantity(self.product, 6)
        # Vérifier que la quantité a bien été mise à jour
        self.assertEqual(self.cart.items[self.product], 6)

    def test_update_quantity_to_negative(self):
        """Test de la mise à jour de la quantité à un nombre négatif"""
        # Ajouter le produit au panier
        self.cart.add_product(self.product, 5)
        # Tenter de mettre à jour la quantité avec un nombre négatif
        with self.assertRaises(ValueError) as context:
            self.cart.update_product_quantity(self.product, -5)
        # Vérifier que l'exception correspond à l'attendu
        self.assertEqual(str(context.exception), "Quantity cannot be negative.")

    def test_update_quantity_to_large_number(self):
        """Test de la mise à jour de la quantité avec un grand nombre"""
        # Ajouter le produit au panier
        self.cart.add_product(self.product, 5)
        # Tenter de mettre à jour la quantité à un grand nombre (au-delà du stock)
        with self.assertRaises(ValueError) as context:
            self.cart.update_product_quantity(self.product, 20)
        # Vérifier que l'exception correspond à l'attendu
        self.assertEqual(str(context.exception), "Cannot update Headphones to 20. Only 10 left.")

if __name__ == '__main__':
    unittest.main()
