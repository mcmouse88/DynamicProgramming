from typing import List


def rob(nums: List[int]) -> int:
    """
    Return the maximum amount of money that can be robbed from houses arranged
    in a circle, without robbing two adjacent houses.

    Because the houses are circular the first and last house are adjacent, so
    they cannot both be robbed. This reduces the problem to two independent
    linear House Robber sub-problems:
      - sub-problem A: houses 0 … n-2  (exclude the last)
      - sub-problem B: houses 1 … n-1  (exclude the first)

    The answer is the maximum of the two results.

    Time:  O(n)
    Space: O(1)

    Args:
        nums: A list of non-negative integers representing the amount of
              money at each house, arranged in a circle.

    Returns:
        The maximum sum achievable without robbing two adjacent houses.

    Example:
        >>> rob([2, 3, 2])
        3
        >>> rob([1, 2, 3, 1])
        4
    """
    if len(nums) < 2:
        return nums[0]

    def helper(arr: List[int]) -> int:
        prev, curr = 0, 0
        for num in arr:
            prev, curr = curr, max(curr, prev + num)
        return curr

    return max(helper(nums[:-1]), helper(nums[1:]))
