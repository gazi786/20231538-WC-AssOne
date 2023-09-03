import pytest
from blackfriday.black_friday import Product, ShoppingCart

""""
In these test cases:

1. test_calculate_total_single_product and test_calculate_total_multiple_products test the calculate_total method for different numbers of products.

2. test_apply_discount_no_discount and test_apply_discount_discount_applied test the apply_discount method with scenarios where the discount should not be applied and where it should be applied, respectively."""


def test_calculate_total_single_product():
    cart = ShoppingCart()
    product = Product("Product 1", 50)
    cart.add_item(product)
    assert cart.calculate_total() == 50


def test_calculate_total_multiple_products():
    cart = ShoppingCart()
    products = [
        Product("Product 1", 50),
        Product("Product 2", 60),
    ]
    for product in products:
        cart.add_item(product)
    assert cart.calculate_total() == 110


def test_apply_discount_no_discount():
    cart = ShoppingCart()
    products = [
        Product("Product 1", 30),
        Product("Product 2", 40),
    ]
    for product in products:
        cart.add_item(product)
    assert cart.apply_discount(50) == 70  # No discount applied


def test_apply_discount_discount_applied():
    cart = ShoppingCart()
    products = [
        Product("Product 1", 50),
        Product("Product 2", 60),
        Product("Product 3", 30),
        Product("Product 4", 40),
        Product("Product 5", 20),
    ]
    for product in products:
        cart.add_item(product)
    assert cart.apply_discount(50) == 210  # Discount of $50 applied


if __name__ == "__main__":
    pytest.main()
