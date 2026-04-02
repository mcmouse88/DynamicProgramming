# Climbing Stairs — Problem Breakdown

## Problem

You are climbing a staircase with `n` steps. Each time you can climb either
**1 or 2 steps**. Return the number of **distinct ways** to reach the top.

**Example:**
```
n = 5

Ways to climb 5 stairs:
  1+1+1+1+1
  1+1+1+2
  1+1+2+1
  1+2+1+1
  2+1+1+1
  1+2+2
  2+1+2
  2+2+1

Answer: 8
```

---

## Key Insight

To reach stair `i` you must have come from either:
- stair `i - 1` (took a 1-step), or
- stair `i - 2` (took a 2-step)

So the number of ways to reach stair `i` is simply the sum of the ways to
reach the two stairs below it:

```
dp[i] = dp[i-1] + dp[i-2]
```

This is exactly the **Fibonacci recurrence**. The answer for `n` stairs is
`fib(n + 1)`.

Base cases: `dp[0] = 1` (one way to stand at the bottom — do nothing),
`dp[1] = 1` (only one way to reach the first stair).

---

## Walkthrough — `n = 5`

We track two variables instead of a full array:
- `prev` — ways to reach the stair two positions back
- `curr` — ways to reach the stair one position back

```
Initial:  prev = 0, curr = 1   (seeds: fib(0)=0, fib(1)=1)

step 1:  prev, curr = 1, 0+1 = 1   → ways to reach stair 1: 1
step 2:  prev, curr = 1, 1+1 = 2   → ways to reach stair 2: 2
step 3:  prev, curr = 2, 1+2 = 3   → ways to reach stair 3: 3
step 4:  prev, curr = 3, 2+3 = 5   → ways to reach stair 4: 5
step 5:  prev, curr = 5, 3+5 = 8   → ways to reach stair 5: 8

return curr = 8
```

---

## Implementation

```python
def climbStairs(n: int) -> int:
    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr
    return curr
```

The parallel assignment `prev, curr = curr, prev + curr` captures the old
values of both variables before either is overwritten — avoiding the need for
a temporary variable.

---

## Complexity

| Metric | Value | Reason                                   |
|--------|-------|------------------------------------------|
| Time   | O(n)  | Single loop over n steps                 |
| Space  | O(1)  | Only two scalar variables, no DP table   |

---

## Edge Cases

| Input | Output | Reason                                       |
|-------|--------|----------------------------------------------|
| `1`   | `1`    | Only one way: take a single 1-step           |
| `2`   | `2`    | Either `1+1` or `2`                          |
| `3`   | `3`    | `1+1+1`, `1+2`, `2+1`                        |
| `45`  | `1836311903` | Large input — still O(n) time         |

---

## Connection to Fibonacci

`climbStairs(n)` returns `fib(n + 1)` where `fib` is the standard Fibonacci
sequence (`fib(1)=1, fib(2)=1, fib(3)=2, ...`).

| n  | climbStairs(n) | fib(n+1) |
|----|---------------|----------|
| 1  | 1             | fib(2)=1 |
| 2  | 2             | fib(3)=2 |
| 3  | 3             | fib(4)=3 |
| 4  | 5             | fib(5)=5 |
| 5  | 8             | fib(6)=8 |
