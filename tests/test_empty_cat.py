import unittest
from product import Product
from cart import Cart

class TestCartMethods(unittest.TestCase):

    def setUp(self):
        """Initialisation avant chaque test"""
        # Création d'un produit pour les tests
        self.product1 = Product("Headphones", 100.0, 10)  # 10 unités disponibles
        self.product2 = Product("Mouse", 25.0, 50)        # 50 unités disponibles
        self.cart = Cart()

    def test_empty_cart(self):
        """Test de la fonctionnalité empty_cart"""
        # Ajouter des produits au panier
        self.cart.add_product(self.product1, 3)  # 3 casques
        self.cart.add_product(self.product2, 5)  # 5 souris

        # Vérifier que le panier contient des articles avant de le vider
        self.assertEqual(len(self.cart.items), 2)  # 2 types de produits dans le panier

        # Vider le panier
        self.cart.empty_cart()

        # Vérifier que le panier est maintenant vide
        self.assertEqual(len(self.cart.items), 0)  # Le panier doit être vide après l'appel de empty_cart

if __name__ == '__main__':
    unittest.main()
