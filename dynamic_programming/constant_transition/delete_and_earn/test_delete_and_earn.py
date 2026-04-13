import pytest
from dynamic_programming.constant_transition.delete_and_earn.delete_and_earn import deleteAndEarn

DELETE_AND_EARN_CASES = [
    # (nums, expected)
    ([3, 4, 2], 6),                  # take 4+2=6; taking 3 blocks both neighbours
    ([2, 2, 3, 3, 3, 4], 9),         # take all 3s (9 pts), blocks 2s and 4s
    ([1, 2, 3], 4),                  # take 1 and 3 (non-adjacent values)
    ([1, 2], 2),                     # two consecutive values — pick the larger gain
    ([2, 1], 2),                     # order in input doesn't matter
    ([1], 1),                        # single element
    ([2], 2),                        # single element, value > 1
    ([1, 1, 1, 2, 4, 4], 11),        # take 1*3=3 (skip 2), then 4*2=8; total 11
    ([1, 3, 5], 9),                  # all non-consecutive — take every value
    ([1, 2, 3, 4, 5], 9),            # alternating: take 1+3+5=9
]


@pytest.mark.parametrize("nums, expected", DELETE_AND_EARN_CASES)
def test_delete_and_earn(nums, expected):
    assert deleteAndEarn(nums) == expected


def test_delete_and_earn_does_not_mutate_input():
    nums = [3, 4, 2]
    original = nums[:]
    deleteAndEarn(nums)
    assert nums == original


def test_delete_and_earn_all_same():
    # All elements equal — no neighbours to block, earn n * val.
    assert deleteAndEarn([5, 5, 5, 5]) == 20


def test_delete_and_earn_large_count():
    # 100 copies of value 2 and 100 copies of value 3.
    # gain(2)=200, gain(3)=300 — consecutive, pick 3.
    nums = [2] * 100 + [3] * 100
    assert deleteAndEarn(nums) == 300


def test_delete_and_earn_non_consecutive_gap():
    # Values 1 and 100 are not consecutive — both can be earned.
    assert deleteAndEarn([1, 100]) == 101
