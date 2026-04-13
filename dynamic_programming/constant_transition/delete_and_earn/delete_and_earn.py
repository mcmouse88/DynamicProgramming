from collections import Counter
from typing import List


def deleteAndEarn(nums: List[int]) -> int:
    """
    Return the maximum points earned by repeatedly deleting elements from nums.

    When you delete an element with value v, every element equal to v-1 or v+1
    is also deleted and you earn v points per deletion.  Grouping all copies of
    v together gives a gain of v * count(v), and the mutual-exclusion rule
    (consecutive values cannot both be chosen) is identical to House Robber on
    the sorted list of distinct values.

    Time:  O(n + k log k)  where k is the number of distinct values
    Space: O(k)

    Args:
        nums: A list of positive integers.

    Returns:
        The maximum total points achievable.

    Example:
        >>> deleteAndEarn([3, 4, 2])
        6
        >>> deleteAndEarn([2, 2, 3, 3, 3, 4])
        9
    """
    count = Counter(nums)
    nums = sorted(count.keys())

    prev, curr = 0, 0

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1] + 1:
            prev, curr = curr, max(curr, prev + num * count[num])
        else:
            prev, curr = curr, curr + num * count[num]
    return curr
