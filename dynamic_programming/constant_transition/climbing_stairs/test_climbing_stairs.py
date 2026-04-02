import pytest
from dynamic_programming.constant_transition.climbing_stairs.climbing_stairs import climbStairs

CLIMB_CASES = [
    # (n, expected)
    (1, 1),    # only one way: [1]
    (2, 2),    # [1,1] or [2]
    (3, 3),    # [1,1,1], [1,2], [2,1]
    (4, 5),    # fib(5)
    (5, 8),    # fib(6)
    (6, 13),   # fib(7)
    (10, 89),  # fib(11)
    (45, 1836311903),  # large input, still O(n)
]


@pytest.mark.parametrize("n, expected", CLIMB_CASES)
def test_climbStairs(n, expected):
    assert climbStairs(n) == expected


def test_climbStairs_fibonacci_relationship():
    # climbStairs(n) == fib(n+1), verified for first 10 values.
    fib = [0, 1]
    for _ in range(10):
        fib.append(fib[-1] + fib[-2])
    for n in range(1, 11):
        assert climbStairs(n) == fib[n + 1]


def test_climbStairs_monotonically_increasing():
    # More stairs → more ways (strictly increasing).
    results = [climbStairs(n) for n in range(1, 11)]
    assert results == sorted(results)
    assert len(set(results)) == len(results)
