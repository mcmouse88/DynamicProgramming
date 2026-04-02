def climbStairs(n: int) -> int:
    """
    Return the number of distinct ways to climb n stairs, taking 1 or 2 steps
    at a time.

    Uses a bottom-up DP approach, keeping only the two most recent values
    instead of a full table — identical in structure to computing Fibonacci
    numbers.

    Time:  O(n)
    Space: O(1)

    Args:
        n: A positive integer representing the total number of stairs.

    Returns:
        The number of distinct step combinations to reach the top.

    Example:
        >>> climbStairs(5)
        8
    """
    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr
    return curr
