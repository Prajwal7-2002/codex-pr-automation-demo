from app.utils import add, apply_discount

def test_add_basic():
    assert add(2, 3) == 5

def test_apply_discount_basic():
    assert apply_discount(100, 0.2) == 80

def test_add_negative():
    assert add(-1, -1) == -2

def test_apply_discount_no_discount():
    assert apply_discount(50, 0) == 50