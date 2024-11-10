from quaternion import Quaternion

def test_add_simple():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    expected = Quaternion(6, 8, 10, 12)
    assert (q1 + q2) == expected

def test_add_zero():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(0, 0, 0, 0)
    assert (q1 + q2) == q1

def test_add_negative():
    q1 = Quaternion(-1, -2, -3, -4)
    q2 = Quaternion(5, 6, 7, 8)
    expected = Quaternion(4, 4, 4, 4)
    assert (q1 + q2) == expected

def test_add_int():
    q1 = Quaternion(1, 2, 3, 4)
    n = 5
    expected = Quaternion(6, 2, 3, 4) 
    assert (q1 + n) == expected

def test_radd_int():
    q1 = Quaternion(1, 2, 3, 4)
    n = 5
    expected = Quaternion(6, 2, 3, 4)
    assert (n + q1) == expected

def test_radd_simple():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    expected = Quaternion(6, 8, 10, 12)
    assert (q2 + q1) == expected

def test_add_invalid_input():
    q1 = Quaternion(1, 2, 3, 4)
    try:
        q1 + "abc"
        assert False, "Ожидалось исключение"
    except TypeError:
        pass # Исключение поймано - это нормально

def test_add_immutability():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    (q1 + q2)
    assert q1 == Quaternion(1, 2, 3, 4)

def test_radd_immutability():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    (q2 + q1)
    assert q2 == Quaternion(5, 6, 7, 8)

def test_sub_simple():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    expected = Quaternion(-4, -4, -4, -4)
    assert (q1 - q2) == expected

def test_rsub_simple():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    expected = Quaternion(4, 4, 4, 4)
    assert (q2 - q1) == expected

def test_sub_scalar():
    q1 = Quaternion(1, 2, 3, 4)
    expected = Quaternion(-4, 2, 3, 4)
    assert (q1 - 5) == expected

def test_rsub_scalar():
    q1 = Quaternion(1, 2, 3, 4)
    expected = Quaternion(4, -2, -3, -4)
    assert (5 - q1) == expected

def test_sub_zero():
    q1 = Quaternion(1, 2, 3, 4)
    result = q1 - Quaternion(0, 0, 0, 0)
    assert result == q1

def test_rsub_zero():
    q1 = Quaternion(1, 2, 3, 4)
    result = q1 - Quaternion(0, 0, 0, 0)
    assert result == q1

def test_sub_self():
    q1 = Quaternion(1, 2, 3, 4)
    result = q1 - q1
    assert result == Quaternion(0, 0, 0, 0)

def test_rsub_self():
    q1 = Quaternion(1, 2, 3, 4)
    result = q1 - q1
    assert result == Quaternion(0, 0, 0, 0)

def test_mul_quaternions():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    result = q1 * q2
    expected_result = Quaternion(-60, 12, 30, 24)
    assert result == expected_result

def test_rmul_quaternions():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    result = q2 * q1
    expected_result = Quaternion(-60, 20, 14, 32)
    assert result == expected_result

def test_mul_scalar():
    q1 = Quaternion(1, 2, 3, 4)
    result = q1 * 5
    expected_result = Quaternion(5, 10, 15, 20)
    assert result == expected_result

def test_rmul_scalar():
    q1 = Quaternion(1, 2, 3, 4)
    result = 5 * q1
    expected_result = Quaternion(5, 10, 15, 20)
    assert result == expected_result

def test_inverse():
    q1 = Quaternion(1, 2, 3, 4)
    result = q1.inverse()
    expected_result = Quaternion(1/30, -1/15, -0.1, -0.1 - 1/30)
    assert result == expected_result

def test_inverse_zero_norm():
    q1 = Quaternion(0, 0, 0, 0)
    try:
        q1.inverse()
        assert False, "Should have raised ZeroDivisionError"
    except ZeroDivisionError:
        assert True

def test_truediv():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    result = q1 / q2
    expected_result = Quaternion(0.402, 0.046, 0.0, 0.092)
    assert result == expected_result

def test_rtruediv():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    result = q2 / q1
    expected_result = Quaternion(7/3, -0.2 - 1/15, 0, -0.5 - 1/30)
    assert result == expected_result

def test_truediv_self():
    q1 = Quaternion(1, 2, 3, 4)
    expected_result = Quaternion(1, 0, 0, 0)
    assert (q1 / q1) == expected_result


def test_truediv_one():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(1, 0, 0, 0)
    result = q1 / q2
    assert result == q1

def test_rtruediv_one():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(1, 0, 0, 0)
    result = q2 / q1
    expected_result = Quaternion(1/30, -1/15, -0.1, -0.1 - 1/30)
    assert result == expected_result

def test_truediv_zero_quaternion():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(0, 0, 0, 0)
    try:
        q1 / q2
        assert False, "Should have raised ZeroDivisionError"
    except ZeroDivisionError:
        assert True


def test_rtruediv_zero_quaternion():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(0, 0, 0, 0)
    result = q2 / q1
    expected_result = Quaternion(0, 0, 0, 0)
    assert result == expected_result

def test_pow_zero():
    q1 = Quaternion(1, 2, 3, 4)
    result = q1 ** 0
    expected_result = Quaternion(1, 0, 0, 0)
    assert result == expected_result

def test_pow_one():
    q1 = Quaternion(1, 2, 3, 4)
    result = q1 ** 1
    assert result == q1

def test_pow_positive():
    q1 = Quaternion(1, 2, 3, 4)
    result = q1 ** 3
    expected_result = Quaternion(-86, -52, -78, -104)
    assert result == expected_result

def test_pow_negative():
    q1 = Quaternion(1, 2, 3, 4)
    result = q1 ** -1
    expected_result = Quaternion(1/30, -2/30, -3/30, -4/30)
    assert result == expected_result

def test_pow_non_integer():
    q1 = Quaternion(1, 2, 3, 4)
    try:
        q1 ** 2.5
        assert False, "Should have raised ValueError"
    except ValueError:
        assert True


if __name__ == "__main__":
    test_add_simple()
    test_add_zero()
    test_add_negative()
    test_radd_simple()
    test_add_invalid_input()
    test_add_immutability()
    test_add_int()
    test_radd_int()
    test_sub_simple()
    test_rsub_simple()
    test_sub_scalar()
    test_rsub_scalar()
    test_sub_zero()
    test_rsub_zero()
    test_sub_self()
    test_rsub_self()
    test_mul_quaternions()
    test_rmul_quaternions()
    test_mul_scalar()
    test_rmul_scalar()
    test_inverse()
    test_inverse_zero_norm()
    test_truediv()
    test_rtruediv()
    test_truediv_self()
    test_truediv_one()
    test_rtruediv_one()
    test_truediv_zero_quaternion()
    test_rtruediv_zero_quaternion()
    test_pow_zero()
    test_pow_one()
    test_pow_positive()
    test_pow_negative()
    test_pow_non_integer()
    print("Все тесты пройдены!")