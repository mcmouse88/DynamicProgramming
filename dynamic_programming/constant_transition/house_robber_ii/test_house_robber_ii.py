import pytest
from dynamic_programming.constant_transition.house_robber_ii.house_robber_ii import rob

ROB_II_CASES = [
    # (nums, expected)
    ([2, 3, 2], 3),               # circular: can't rob both ends; best = house 1 (3)
    ([1, 2, 3, 1], 4),            # rob house 0 (1) + house 2 (3) = 4
    ([1, 2, 3], 3),               # rob house 2 (3) only
    ([0], 0),                     # single house, zero money
    ([5], 5),                     # single house
    ([2, 1], 2),                  # two houses — pick the larger
    ([1, 2], 2),                  # two houses — pick the larger
    ([2], 2),                     # single house with positive value
    ([0, 0, 0], 0),               # all zeros
    ([1, 1, 1, 1], 2),            # circular, alternating — rob houses 0 and 2 (or 1 and 3)
    ([200, 3, 140, 20, 10], 340),  # rob house 0 (200) + house 2 (140) = 340
]


@pytest.mark.parametrize("nums, expected", ROB_II_CASES)
def test_rob(nums, expected):
    assert rob(nums) == expected


def test_rob_does_not_mutate_input():
    nums = [2, 3, 2]
    original = nums[:]
    rob(nums)
    assert nums == original


def test_rob_long_alternating():
    # Houses in a circle: all odd-indexed have value 0, all even-indexed have value 1.
    # With circular constraint the answer is still n // 2 for large enough n.
    nums = [1, 0] * 50            # 100 houses arranged in a circle, max = 50
    assert rob(nums) == 50


def test_rob_single_large_value():
    assert rob([0, 0, 1000, 0, 0]) == 1000
