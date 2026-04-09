from typing import List


def minCostClimbingStairsTopDown(cost: List[int]) -> int:
    """
    Return the minimum cost to reach the top of the staircase.

    You may start from step 0 or step 1 at no extra cost. Paying cost[i]
    lets you climb one or two steps from step i. The top is the floor
    beyond the last index.

    Uses top-down DP (memoization): dp[i] is the minimum cost to land on
    step i. The base case i < 0 returns 0, naturally encoding the free
    start from step 0 or step 1.

    Recurrence:
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    Time:  O(n)
    Space: O(n)

    Args:
        cost: A list of non-negative integers where cost[i] is the cost of
              stepping on stair i.

    Returns:
        The minimum total cost to reach the top.

    Example:
        >>> minCostClimbingStairsTopDown([10, 15, 20])
        15
        >>> minCostClimbingStairsTopDown([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        6
    """
    n = len(cost)
    dp = [-1] * n

    def top_down(i):
        if i < 0:
            return 0
        if dp[i] != -1:
            return dp[i]

        dp[i] = cost[i] + min(top_down(i - 1), top_down(i - 2))
        return dp[i]

    top_down(n - 1)
    return min(dp[n - 1], dp[n - 2])


def minCostClimbingStairs(cost: List[int]) -> int:
    """
    Return the minimum cost to reach the top of the staircase.

    Space-optimized bottom-up DP: two variables track the minimum cost to
    land on the previous two steps, replacing the full dp table. Initializing
    both to 0 encodes the free start from step 0 or step 1.

    Recurrence:
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    Time:  O(n)
    Space: O(1)

    Args:
        cost: A list of non-negative integers where cost[i] is the cost of
              stepping on stair i.

    Returns:
        The minimum total cost to reach the top.

    Example:
        >>> minCostClimbingStairs([10, 15, 20])
        15
        >>> minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        6
    """
    prev, curr = 0, 0
    for step in cost:
        prev, curr = curr, step + min(prev, curr)
    return min(prev, curr)
