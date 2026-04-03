import pytest
from dynamic_programming.constant_transition.n_tribonacci_number.n_tribonacci_number import tribonacci

TRIBONACCI_SEQUENCE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 4),
    (5, 7),
    (6, 13),
    (7, 24),
    (10, 149),
    (25, 1389537),
    (37, 2082876103),
]


@pytest.mark.parametrize("n, expected", TRIBONACCI_SEQUENCE)
def test_tribonacci(n, expected):
    assert tribonacci(n) == expected
