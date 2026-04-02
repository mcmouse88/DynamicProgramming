import pytest
from dynamic_programming.constant_transition.memoized_fibonacci.memoized_fibonacci import (
    fibonacci_memo,
    fibonacci_cache,
)

FIBONACCI_CASES = [
    # (n, expected)
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


@pytest.mark.parametrize("n, expected", FIBONACCI_CASES)
def test_fibonacci_memo(n, expected):
    assert fibonacci_memo(n) == expected


@pytest.mark.parametrize("n, expected", FIBONACCI_CASES)
def test_fibonacci_cache(n, expected):
    assert fibonacci_cache(n) == expected


def test_both_implementations_agree():
    for n in range(30):
        assert fibonacci_memo(n) == fibonacci_cache(n)


def test_fibonacci_memo_repeated_calls():
    # Calling multiple times should return the same result (cache is local).
    assert fibonacci_memo(10) == fibonacci_memo(10) == 55


def test_fibonacci_cache_repeated_calls():
    # @cache persists across calls — results must remain consistent.
    assert fibonacci_cache(10) == fibonacci_cache(10) == 55
