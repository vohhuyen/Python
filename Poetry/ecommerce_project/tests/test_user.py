from ecommerce_project.user import UserManager

def test_add_user():
    user_manager = UserManager()
    user_manager.add_user("JaneDoe", "jane@example.com")
    user = user_manager.get_user(2)
    assert user['username'] == "JaneDoe"
