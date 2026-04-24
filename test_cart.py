import pytest
from cart import ShoppingCart

def test_add_item_and_total():
    cart = ShoppingCart()
    cart.add_item("apple", 10.0, 2)
    assert cart.get_total() == 20.0

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("apple", 10.0, 1)
    cart.remove_item("apple")
    assert cart.get_total() == 0.0

def test_apply_valid_discount_percent():
    cart = ShoppingCart()
    cart.add_item("item", 100.0, 1)
    cart.apply_discount("SAVE10")
    assert cart.get_total() == 90.0

def test_apply_valid_discount_fixed():
    cart = ShoppingCart()
    cart.add_item("item", 40.0, 1)
    cart.apply_discount("FLAT5")
    assert cart.get_total() == 35.0

def test_add_item_zero_quantity():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item("apple", 10.0, 0)

def test_add_item_negative_quantity():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item("apple", 10.0, -1)

def test_add_item_negative_price():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item("apple", -10.0, 1)

def test_remove_nonexistent_item():
    cart = ShoppingCart()
    with pytest.raises(KeyError):
        cart.remove_item("banana")



def test_invalid_discount_code():
    cart = ShoppingCart()
    cart.add_item("item", 20.0, 1)
    with pytest.raises(ValueError):
        cart.apply_discount("INVALID")

def test_discount_below_minimum():
    cart = ShoppingCart()
    cart.add_item("item", 20.0, 1)
    with pytest.raises(ValueError):
        cart.apply_discount("SAVE20")



def test_add_same_item_twice_updates_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 10.0, 1)
    cart.add_item("apple", 10.0, 5)
    assert cart.get_total() == 50.0

def test_clear_cart():
    cart = ShoppingCart()
    cart.add_item("apple", 10.0, 2)
    cart.clear()
    assert cart.get_total() == 0.0

def test_get_item_count():
    cart = ShoppingCart()
    cart.add_item("apple", 10.0, 2)
    cart.add_item("banana", 5.0, 3)

    assert cart.get_item_count() == 5

def test_apply_multiple_discounts_not_allowed():
    cart = ShoppingCart()
    cart.add_item("item", 100.0, 1)

    cart.apply_discount("SAVE10")

    with pytest.raises(ValueError):
        cart.apply_discount("FLAT5")


def test_discount_exact_threshold():
    cart = ShoppingCart()
    cart.add_item("item", 50.0, 1)

    cart.apply_discount("SAVE20")

    assert cart.get_total() == 40.0

def test_and_get_item_implement():
    cart = ShoppingCart()
    cart.add_item("Book", 10.0, 2)
    cart.add_item("Pen", 10.0, 2)

    count = cart.get_item_count()

    assert count == 4