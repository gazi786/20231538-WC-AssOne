class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def calculate_total(self):
        # Calculate the total purchase value
        pass

    def apply_discount(self, discount_amount):
        # Apply the discount if conditions are met
        pass
