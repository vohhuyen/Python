class Product:
    def __init__(self, product_id, name, description, price, stock):
        self.id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"<Product {self.name} (${self.price})>"

class User:
    def __init__(self, user_id, username, email, cart=None):
        self.id = user_id
        self.username = username
        self.email = email
        self.cart = cart if cart else []

    def __repr__(self):
        return f"<User {self.username}>"

class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def __repr__(self):
        return f"<Cart for User {self.user_id}, {len(self.items)} items>"
