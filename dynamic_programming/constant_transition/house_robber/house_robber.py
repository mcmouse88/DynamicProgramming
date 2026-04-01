from typing import List


def rob(nums: List[int]) -> int:
    """
    Return the maximum amount of money that can be robbed without robbing
    two adjacent houses.

    Uses a bottom-up DP approach, keeping only the two most recent
    optimal values instead of a full table.

    Time:  O(n)
    Space: O(1)

    Args:
        nums: A list of non-negative integers representing the amount of
              money at each house.

    Returns:
        The maximum sum achievable by choosing non-adjacent elements.

    Example:
        >>> rob([2, 7, 9, 3, 1])
        12
    """
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr
