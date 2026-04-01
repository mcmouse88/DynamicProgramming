import pytest
from dynamic_programming.constant_transition.house_robber.house_robber import rob

ROB_CASES = [
    # (nums, expected)
    ([1, 2, 3, 1], 4),          # rob house 0 (1) + house 2 (3) = 4
    ([2, 7, 9, 3, 1], 12),      # rob house 0 (2) + house 2 (9) + house 4 (1) = 12
    ([0], 0),                   # single house, zero money
    ([5], 5),                   # single house
    ([2, 1], 2),                # two houses — pick the larger
    ([1, 2], 2),                # two houses — pick the larger
    ([0, 0, 0], 0),             # all zeros
    ([10, 1, 1, 10], 20),       # rob both ends
    ([2, 1, 1, 2], 4),          # symmetric — rob both ends
    ([100, 1, 1, 100], 200),    # large values at both ends
]


@pytest.mark.parametrize("nums, expected", ROB_CASES)
def test_rob(nums, expected):
    assert rob(nums) == expected


def test_rob_does_not_mutate_input():
    nums = [2, 7, 9, 3, 1]
    original = nums[:]
    rob(nums)
    assert nums == original


def test_rob_long_alternating():
    # All odd-indexed houses have value 0; all even-indexed have value 1.
    # Optimal: rob every even-indexed house.
    nums = [1, 0] * 50          # 100 houses, max = 50
    assert rob(nums) == 50


def test_rob_single_large_value():
    assert rob([0, 0, 1000, 0, 0]) == 1000
