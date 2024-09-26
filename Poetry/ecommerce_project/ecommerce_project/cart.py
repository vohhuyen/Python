from ecommerce_project.database import Database

class CartManager:
    def __init__(self):
        self.db = Database()

    def add_to_cart(self, user_id, product_id, quantity):
        user = next((u for u in self.db.data['users'] if u['id'] == user_id), None)
        product = next((p for p in self.db.data['products'] if p['id'] == product_id), None)
        if user and product:
            user['cart'].append({"product_id": product_id, "quantity": quantity})
            self.db.save_data()

    def view_cart(self, user_id):
        user = next((u for u in self.db.data['users'] if u['id'] == user_id), None)
        return user['cart'] if user else None
