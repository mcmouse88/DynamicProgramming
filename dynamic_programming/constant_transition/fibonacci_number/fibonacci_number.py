def bottom_up(n: int) -> int:
    """
    Return the n-th Fibonacci number using a bottom-up iterative approach.

    Builds the solution from the base cases upward, keeping only the
    previous two values at each step.

    Time:  O(n)
    Space: O(1)

    Args:
        n: A non-negative integer index in the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number.

    Example:
        >>> bottom_up(6)
        8
    """
    if n < 2:
        return n
    prev, curr = 0, 1

    for num in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


class TopDown:
    """
    Compute Fibonacci numbers using a top-down recursive approach with memoization.

    Results are cached in an instance dictionary to avoid recomputing
    the same subproblems across calls.

    Time:  O(n)
    Space: O(n)
    """

    def __init__(self):
        self.cache = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        """
        Return the n-th Fibonacci number.

        Args:
            n: A non-negative integer index in the Fibonacci sequence.

        Returns:
            The n-th Fibonacci number.

        Example:
            >>> TopDown().fib(6)
            8
        """
        if n in self.cache:
            return self.cache[n]
        res = self.fib(n - 1) + self.fib(n - 2)
        self.cache[n] = res
        return res
