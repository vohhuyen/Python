from ecommerce_project.database import Database

class UserManager:
    def __init__(self):
        self.db = Database()

    def add_user(self, username, email):
        user_id = len(self.db.data['users']) + 1
        new_user = {
            'id': user_id,
            'username': username,
            'email': email,
            'cart': []
        }
        self.db.data['users'].append(new_user)
        self.db.save_data()

    def get_user(self, user_id):
        return next((u for u in self.db.data['users'] if u['id'] == user_id), None)

    def update_user(self, user_id, username=None, email=None):
        user = self.get_user(user_id)
        if user:
            if username: user['username'] = username
            if email: user['email'] = email
            self.db.save_data()
        return user
