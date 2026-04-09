import pytest
from dynamic_programming.constant_transition.min_cost_climbing_stairs.min_cost_climbing_stairs import (
    minCostClimbingStairs,
    minCostClimbingStairsTopDown,
)

MIN_COST_CASES = [
    # (cost, expected)
    ([10, 15, 20], 15),                              # start at 1 (15), jump 2 → top
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),       # skip the 100s
    ([1, 2], 1),                                     # start at 0 (1), jump 2 → top
    ([2, 1], 1),                                     # start at 1 (1), jump 1 → top
    ([0, 0, 0], 0),                                  # all zeros
    ([10, 15], 10),                                  # start at 0 (10), jump 2 → top
    ([5, 5, 5], 5),                                  # any single step costs 5
    ([1, 1, 1, 1], 2),                               # alternating steps: 1 + 1 = 2
    ([0, 1, 0, 1], 0),                               # skip cost-1 steps entirely
    ([100, 0, 100, 0], 0),                           # free steps at index 1 and 3
]


@pytest.mark.parametrize("cost, expected", MIN_COST_CASES)
def test_min_cost_climbing_stairs(cost, expected):
    assert minCostClimbingStairs(cost) == expected


@pytest.mark.parametrize("cost, expected", MIN_COST_CASES)
def test_min_cost_climbing_stairs_top_down(cost, expected):
    assert minCostClimbingStairsTopDown(cost) == expected


def test_does_not_mutate_input():
    cost = [10, 15, 20]
    original = cost[:]
    minCostClimbingStairs(cost)
    assert cost == original


def test_top_down_does_not_mutate_input():
    cost = [10, 15, 20]
    original = cost[:]
    minCostClimbingStairsTopDown(cost)
    assert cost == original


def test_large_uniform_cost():
    # All steps cost 1; optimal path skips every other step: ceil(n/2) * 1
    # For n=100 steps, best is 50 (start at 0 or 1, jump by 2 each time)
    cost = [1] * 100
    assert minCostClimbingStairs(cost) == 50
    assert minCostClimbingStairsTopDown(cost) == 50


def test_both_implementations_agree():
    import random
    random.seed(42)
    for _ in range(20):
        cost = [random.randint(0, 999) for _ in range(random.randint(2, 30))]
        assert minCostClimbingStairs(cost) == minCostClimbingStairsTopDown(cost)
