from Library import Library


def test_add(lib, other, expected_result):
    result = lib + other
    assert result.quantity == expected_result, f"ожидал {expected_result}, но получил {result.quantity} для {lib.quantity} + {other}"

def test_sub(lib, other, expected_result):
    result = lib - other
    assert result.quantity == expected_result, f"ожидал {expected_result}, но получил {result.quantity} для {lib.quantity} - {other}"

def test_iadd(lib, other, expected_result):
    lib += other
    assert lib.quantity == expected_result, f"ожидал {expected_result}, но получил {lib.quantity} для {lib.quantity} += {other}"

def test_isub(lib, other, expected_result):
    lib -= other
    assert lib.quantity == expected_result, f"ожидал {expected_result}, но получил {lib.quantity} для {lib.quantity} -= {other}"

def test_lt(lib, other, expected_result):
    result = lib.quantity < other.quantity
    assert result == expected_result, f"ожидал {expected_result}, но получил {result} для {lib.quantity} < {other.quantity}"

def test_gt(lib, other, expected_result):
    result = lib.quantity > other.quantity
    assert result == expected_result, f"ожидал {expected_result}, но получил {result} для {lib.quantity} > {other.quantity}"

def test_le(lib, other, expected_result):
    result = lib.quantity <= other.quantity
    assert result == expected_result, f"ожидал {expected_result}, но получил {result} для {lib.quantity} <= {other.quantity}"

def test_ge(lib, other, expected_result):
    result = lib.quantity >= other.quantity
    assert result == expected_result, f"ожидал {expected_result}, но получил {result} для {lib.quantity} >= {other.quantity}"

def test_eq(lib, other, expected_result):
    result = lib.quantity == other.quantity
    assert result == expected_result, f"ожидал {expected_result}, но получил {result} для {lib.quantity} == {other.quantity}"

def test_ne(lib, other, expected_result):
    result = lib.quantity != other.quantity
    assert result == expected_result, f"ожидал {expected_result}, но получил {result} для {lib.quantity} != {other.quantity}"


lib = Library("Детская районная", "ул. Кирова, 45", 35)
lib2 = Library("Взрослая", "ул. Достоевского, 100", 5)

test_add(lib, 10, 45)
#test_add(lib, 10, 55)

test_sub(lib, 10, 25)
#test_sub(lib, 10, 35)

test_iadd(lib, 10, 45)
#test_iadd(lib, 10, 55)

test_isub(lib, 10, 35)
#test_isub(lib, 10, 45)

test_lt(lib, lib2, False)
#test_lt(lib, lib2, True)

test_gt(lib, lib2, True)
#test_gt(lib, lib2, False)

test_le(lib, lib2, False)
#test_le(lib, lib2, True)

test_ge(lib, lib2, True)
#test_ge(lib, lib2, False)

test_eq(lib, lib2, False)
#test_eq(lib, lib2, True)

test_ne(lib, lib2, True)
#test_ne(lib, lib2, False)




