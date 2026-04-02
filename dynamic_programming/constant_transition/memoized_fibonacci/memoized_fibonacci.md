# Memoized Fibonacci — Problem Breakdown

## Problem

Implement a memoized version of the Fibonacci function. Without memoization,
the naive recursive solution recomputes the same subproblems exponentially.
The goal is to cache results so each subproblem is solved only once.

**Fibonacci sequence:** `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...`

```
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)   for n >= 2
```

---

## The Problem with Naive Recursion

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)   # O(2^n) — recomputes everything
```

Computing `fib(6)` builds this call tree:

```
                     fib(6)
                   /        \
              fib(5)          fib(4)
             /     \         /     \
         fib(4)  fib(3)  fib(3)  fib(2)
         ...
```

`fib(4)` is computed **twice**, `fib(3)` **three times**, and so on.
Time complexity explodes to **O(2ⁿ)**.

---

## Key Insight — Top-Down DP (Memoization)

Store each result the first time it is computed. On subsequent calls,
return the cached value in O(1) instead of recomputing.

```
fib(6)
  → fib(5)  [not cached, compute]
    → fib(4)  [not cached, compute]
      → fib(3)  [not cached, compute]
        → fib(2)  [not cached, compute]
          → fib(1) = 1  ✓
          → fib(0) = 0  ✓
        cache[2] = 1
      cache[3] = 2
    cache[4] = 3
  cache[5] = 5
  → fib(4)  [cached → 3]  ✓ no recomputation
cache[6] = 8
```

Each value is computed exactly **once** → **O(n)** time.

---

## Two Approaches

### Approach 1 — Manual dict memoization

```python
def fibonacci_memo(n: int) -> int:
    memo = {0: 0, 1: 1}

    def fib(num: int) -> int:
        if num in memo:
            return memo[num]
        memo[num] = fib(num - 1) + fib(num - 2)
        return memo[num]

    return fib(n)
```

The nested `fib` function closes over `memo`. Base cases (`0` and `1`) are
pre-seeded so no explicit `if n <= 1` guard is needed inside the recursion.

---

### Approach 2 — `@functools.lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cache(n: int) -> int:
    if n in (0, 1):
        return n
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)
```

`@lru_cache(maxsize=None)` transparently wraps the function with an unbounded
cache — no manual dict management needed. (`@cache`, available from Python 3.9,
is a shorthand for exactly this.)

---

## Walkthrough — `n = 6`

| Call         | Cached? | Returns |
|--------------|---------|---------|
| `fib(6)`     | No      | 8       |
| `fib(5)`     | No      | 5       |
| `fib(4)`     | No      | 3       |
| `fib(3)`     | No      | 2       |
| `fib(2)`     | No      | 1       |
| `fib(1)`     | Yes (seed) | 1    |
| `fib(0)`     | Yes (seed) | 0    |
| `fib(2)`     | Yes     | 1       |
| `fib(3)`     | Yes     | 2       |
| `fib(4)`     | Yes     | 3       |

Total unique calls: **n + 1** (one per value from 0 to n).

---

## Complexity

| Metric | Naive recursion | Memoized |
|--------|----------------|----------|
| Time   | O(2ⁿ)          | O(n)     |
| Space  | O(n) call stack | O(n) cache + call stack |

---

## Edge Cases

| Input | Output | Reason                  |
|-------|--------|-------------------------|
| `0`   | `0`    | Base case               |
| `1`   | `1`    | Base case               |
| `2`   | `1`    | `fib(1) + fib(0) = 1`   |
| `10`  | `55`   | Standard sequence value |
