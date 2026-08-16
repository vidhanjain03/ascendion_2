from discount import discount_price

def test_discount_price_basic():
    assert discount_price(100, 20) == 80

def test_discount_price_fifty_percent():
    assert discount_price(200, 50) == 100

def test_discount_price_zero_percent():
    assert discount_price(100, 0) == 100