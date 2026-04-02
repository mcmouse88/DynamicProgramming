from functools import lru_cache


def fibonacci_memo(n: int) -> int:
    """
    Return the n-th Fibonacci number using explicit dict-based memoization.

    A nested helper function checks a shared dictionary before recursing,
    storing each computed value so it is never recalculated.

    Time:  O(n)
    Space: O(n) — memo dict and call stack both grow to depth n

    Args:
        n: A non-negative integer index in the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number (fib(0)=0, fib(1)=1).

    Example:
        >>> fibonacci_memo(6)
        8
    """
    memo = {0: 0, 1: 1}

    def fib(num: int) -> int:
        if num in memo:
            return memo[num]
        memo[num] = fib(num - 1) + fib(num - 2)
        return memo[num]

    return fib(n)


@lru_cache(maxsize=None)
def fibonacci_cache(n: int) -> int:
    """
    Return the n-th Fibonacci number using ``functools.lru_cache`` memoization.

    ``@lru_cache(maxsize=None)`` transparently wraps the function with an
    unbounded cache, making it functionally equivalent to manual dict
    memoization but with no boilerplate.

    Time:  O(n)
    Space: O(n) — cache and call stack both grow to depth n

    Args:
        n: A non-negative integer index in the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number (fib(0)=0, fib(1)=1).

    Example:
        >>> fibonacci_cache(6)
        8
    """
    if n in (0, 1):
        return n
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)
