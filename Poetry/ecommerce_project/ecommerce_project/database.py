import json
import os

class Database:
    def __init__(self, filepath='data/data.json'):
        self.filepath = filepath
        self.load_data()

    def load_data(self):
        """Tải dữ liệu từ file JSON, nếu không có file thì tạo mới."""
        if not os.path.exists(self.filepath):
            self.data = {'products': [], 'users': [], 'cart': []}
            self.save_data()
        else:
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)

    def save_data(self):
        """Lưu dữ liệu hiện tại vào file JSON."""
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)

    # CRUD cho sản phẩm
    def add_product(self, name, description, price, stock):
        product_id = len(self.data['products']) + 1
        new_product = {
            'id': product_id,
            'name': name,
            'description': description,
            'price': price,
            'stock': stock
        }
        self.data['products'].append(new_product)
        self.save_data()

    def get_products(self):
        return self.data['products']

    def get_product(self, product_id):
        return next((p for p in self.data['products'] if p['id'] == product_id), None)

    def update_product(self, product_id, name=None, description=None, price=None, stock=None):
        product = self.get_product(product_id)
        if product:
            if name: product['name'] = name
            if description: product['description'] = description
            if price: product['price'] = price
            if stock: product['stock'] = stock
            self.save_data()
        return product

    def delete_product(self, product_id):
        self.data['products'] = [p for p in self.data['products'] if p['id'] != product_id]
        self.save_data()

    # CRUD cho người dùng và giỏ hàng có thể thêm ở đây
