import unittest
from product import Product
from cart import Cart
from order import Order

class TestInvoice(unittest.TestCase):
    def setUp(self):
        """Configure les éléments pour les tests."""
        self.p1 = Product("Laptop", 1200.0, 5)
        self.p2 = Product("Mouse", 25.0, 50)
        self.cart = Cart()

    def test_invoice_with_discount(self):
        """Tester la génération d'une facture avec une remise appliquée."""
        self.cart.add_product(self.p1, 1)
        self.cart.add_product(self.p2, 2)
        order = Order(self.cart, discount_percentage=10)

        expected_invoice = (
            "\n--- Facture ---\n"
            "Items:\n"
            " - Laptop x 1 @ 1200.00€ each = 1200.00€\n"
            " - Mouse x 2 @ 25.00€ each = 50.00€\n"
            "\nSubtotal: 1250.00€"
            "\nDiscount: 10.00%"
            "\nTotal: 1125.00€"
            "\n--- Merci pour votre commande! ---\n"
        )
        invoice = order.generate_invoice()
        self.assertEqual(invoice.strip(), expected_invoice.strip())

    def test_invoice_without_discount(self):
        """Tester la génération d'une facture sans remise."""
        self.cart.add_product(self.p1, 1)
        self.cart.add_product(self.p2, 2)
        order = Order(self.cart, discount_percentage=0)

        expected_invoice = (
            "\n--- Facture ---\n"
            "Items:\n"
            " - Laptop x 1 @ 1200.00€ each = 1200.00€\n"
            " - Mouse x 2 @ 25.00€ each = 50.00€\n"
            "\nSubtotal: 1250.00€"
            "\nDiscount: 0.00%"
            "\nTotal: 1250.00€"
            "\n--- Merci pour votre commande! ---\n"
        )
        invoice = order.generate_invoice()
        self.assertEqual(invoice.strip(), expected_invoice.strip())


if __name__ == "__main__":
    unittest.main()
