from app.utils import add, apply_discount

def test_add_basic():
    assert add(2, 3) == 5

def test_apply_discount_basic():
    assert apply_discount(100, 0.2) == 80

def test_add_negative():
    assert add(-1, -1) == -2

def test_apply_discount_no_discount():
    assert apply_discount(50, 0) == 50


def test_add_zero():
    assert add(0, 5) == 5

def test_apply_discount_full():
    assert apply_discount(200, 1) == 0

def test_add_floats():
    assert add(2.5, 3.5) == 6.0

def test_apply_discount_floats():
    assert apply_discount(99.99, 0.15) == 84.9915