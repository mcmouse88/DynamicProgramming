# Min Cost Climbing Stairs — Problem Breakdown

## Problem

You are given an array `cost` where `cost[i]` is the cost of stepping on
stair `i`. Once you pay the cost, you can climb **one or two steps**.

You may start from **step 0 or step 1** at no extra charge. Return the
**minimum total cost** to reach the top — the floor just beyond the last
index.

**Example:**
```
cost = [10, 15, 20]

Options:
  start at 0 (pay 10), climb 1 → step 1 (pay 15), climb 1 → top  total = 25
  start at 0 (pay 10), climb 2 → step 2 (pay 20), climb 1 → top  total = 30
  start at 1 (pay 15), climb 2 → top                              total = 15  ✓

Answer: 15
```

---

## Key Insight

Define `dp[i]` = minimum cost to **land on** step `i` (including paying `cost[i]`).

From step `i` you could have arrived from step `i-1` or step `i-2`:

```
dp[i] = cost[i] + min(dp[i-1], dp[i-2])
```

The free start from step 0 or step 1 is handled by the base case:
```
dp[i] = 0   for i < 0
```
This makes `dp[0] = cost[0] + min(0, 0) = cost[0]` and
`dp[1] = cost[1] + min(cost[0], 0) = cost[1]`, which is correct — you
can reach step 1 for free by starting there.

After filling the table the answer is:
```
min(dp[n-1], dp[n-2])
```
because from either of those steps you can reach the top in one jump.

---

## Walkthrough — `cost = [10, 15, 20]`

```
i = 0:  dp[0] = 10 + min(0,  0)  = 10
i = 1:  dp[1] = 15 + min(10, 0)  = 15
i = 2:  dp[2] = 20 + min(15, 10) = 30

answer = min(dp[1], dp[2]) = min(15, 30) = 15  ✓
```

---

## Walkthrough — `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]`

```
i = 0:  dp[0]  = 1   + min(0,  0)  = 1
i = 1:  dp[1]  = 100 + min(1,  0)  = 100
i = 2:  dp[2]  = 1   + min(100, 1) = 2
i = 3:  dp[3]  = 1   + min(2, 100) = 3
i = 4:  dp[4]  = 1   + min(3,   2) = 3
i = 5:  dp[5]  = 100 + min(3,   3) = 103
i = 6:  dp[6]  = 1   + min(103, 3) = 4
i = 7:  dp[7]  = 1   + min(4, 103) = 5
i = 8:  dp[8]  = 100 + min(5,   4) = 104
i = 9:  dp[9]  = 1   + min(104, 5) = 6

answer = min(dp[8], dp[9]) = min(104, 6) = 6  ✓
```

---

## Implementation

### Top-Down (Memoization) — O(n) space

```python
def minCostClimbingStairsTopDown(cost: List[int]) -> int:
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
```

### Bottom-Up (Space-Optimized) — O(1) space

```python
def minCostClimbingStairs(cost: List[int]) -> int:
    prev, curr = 0, 0
    for step in cost:
        prev, curr = curr, step + min(prev, curr)
    return min(prev, curr)
```

`prev` and `curr` correspond to `dp[i-2]` and `dp[i-1]` at each iteration.
After the loop, `curr` = `dp[n-1]` and `prev` = `dp[n-2]`.

---

## Complexity

| Implementation | Time | Space |
|----------------|------|-------|
| Top-down (memoization) | O(n) | O(n) — dp table + call stack |
| Bottom-up (space-optimized) | O(n) | O(1) — two scalar variables |

---

## Edge Cases

| Input          | Output | Reason                                            |
|----------------|--------|---------------------------------------------------|
| `[1, 2]`       | `1`    | Start at step 0 (pay 1), jump 2 to top            |
| `[2, 1]`       | `1`    | Start at step 1 (pay 1), jump 1 to top            |
| `[10, 15]`     | `10`   | Start at step 0 (pay 10), jump 2 to top           |
| `[0, 0, 0]`    | `0`    | All steps free — cost is zero                     |
| `[1, 100, 1]`  | `2`    | Start at 0 (pay 1), skip 100, pay 1 at step 2     |
