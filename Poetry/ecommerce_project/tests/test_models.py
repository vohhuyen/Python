from ecommerce_project.models import Product

def test_product():
    product = Product(1, "Laptop", "High-performance laptop", 1500, 10)
    assert product.name == "Laptop"
    assert product.price == 1500
