from ecommerce_project.cart import CartManager

def test_add_to_cart():
    cart_manager = CartManager()
    cart_manager.add_to_cart(1, 1, 1)
    cart = cart_manager.view_cart(1)
    assert len(cart) == 1
