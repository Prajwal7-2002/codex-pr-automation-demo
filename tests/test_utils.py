from app.utils import add, apply_discount

def test_add_basic():
    assert add(2, 3) == 5

def test_apply_discount_basic():
    assert apply_discount(100, 0.2) == 80
