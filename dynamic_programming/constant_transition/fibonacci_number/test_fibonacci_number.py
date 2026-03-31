import pytest
from dynamic_programming.constant_transition.fibonacci_number.fibonacci_number import bottom_up, TopDown

FIBONACCI_SEQUENCE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (10, 55),
    (20, 6765),
]


@pytest.mark.parametrize("n, expected", FIBONACCI_SEQUENCE)
def test_bottom_up(n, expected):
    assert bottom_up(n) == expected


@pytest.mark.parametrize("n, expected", FIBONACCI_SEQUENCE)
def test_top_down(n, expected):
    assert TopDown().fib(n) == expected


def test_top_down_cache_is_reused():
    solver = TopDown()
    assert solver.fib(10) == 55
    assert solver.fib(10) == 55
    assert 10 in solver.cache
