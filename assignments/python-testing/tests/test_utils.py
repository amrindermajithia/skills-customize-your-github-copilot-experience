from assignments.python_testing.starter_code import is_palindrome, factorial, unique_sorted, flatten


def test_is_palindrome_simple():
    assert is_palindrome("Racecar")


def test_is_palindrome_non_alpha():
    assert is_palindrome("A man, a plan, a canal: Panama")


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_positive():
    assert factorial(5) == 120


def test_factorial_negative_raises():
    import pytest
    with pytest.raises(ValueError):
        factorial(-1)


def test_unique_sorted():
    assert unique_sorted([3, 1, 2, 3, 2]) == [1, 2, 3]


def test_flatten():
    assert flatten([[1, 2], [3], []]) == [1, 2, 3]
