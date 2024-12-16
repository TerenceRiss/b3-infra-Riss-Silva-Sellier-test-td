# cart.py

from product import Product

class Cart:
    def __init__(self):
        self.items = {}  # {product: quantity}

    def update_product_quantity(self, product: Product, new_quantity: int):
        """
        Met à jour la quantité d'un produit dans le panier.
        """
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if product.stock < new_quantity:
            raise ValueError(f"Cannot update {product.name} to {new_quantity}. Only {product.stock} left.")
        if new_quantity == 0:
            self.remove_product(product)
        else:
            if product in self.items:
                self.items[product] = new_quantity
            else:
                raise KeyError(f"{product.name} is not in the cart.")


    def add_product(self, product: Product, quantity: int):
        if product.stock < quantity:
            raise ValueError(f"Cannot add {quantity} of {product.name}. Only {product.stock} left.")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product: Product):
        if product in self.items:
            del self.items[product]
        else:
            raise KeyError(f"{product.name} is not in the cart.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def display_cart(self):
        if not self.items:
            return "Your cart is empty."
        return "\n".join([f"{product.name} x {quantity} - {product.price * quantity}€"
                          for product, quantity in self.items.items()])
