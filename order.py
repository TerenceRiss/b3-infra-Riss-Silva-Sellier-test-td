from cart import Cart

class Order:
    def __init__(self, cart: Cart, discount_percentage: float = 0):
        if not cart.items:
            raise ValueError("Cart is empty. Cannot place an order.")
        
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        self.items = cart.items
        self.discount_percentage = discount_percentage
        self.subtotal = cart.calculate_total()
        self.total = self.apply_discount()

    def apply_discount(self):
        """Applique la remise au sous-total."""
        discount = (self.discount_percentage / 100) * self.subtotal
        return self.subtotal - discount

    def place_order(self):
        """Place la commande et met à jour les stocks des produits."""
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)
        return f"Order placed successfully! Total after discount: {self.total:.2f}€"

    def view_order(self):
        """Affiche les détails de la commande, y compris la remise."""
        items_details = "\n".join([f"{product.name} x {quantity}" for product, quantity in self.items.items()])
        return (
            f"{items_details}\n"
            f"Subtotal: {self.subtotal:.2f}€\n"
            f"Discount: {self.discount_percentage}%\n"
            f"Total: {self.total:.2f}€"
        )
