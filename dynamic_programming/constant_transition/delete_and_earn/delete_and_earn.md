# Delete and Earn — Problem Breakdown

## Problem

Given an integer array `nums`, you can perform the following operation any number
of times: pick any `nums[i]`, earn `nums[i]` points, then **delete every element
equal to `nums[i] - 1` and `nums[i] + 1`** from the array.

Return the **maximum total points** you can earn.

**Example 1:**
```
nums = [3, 4, 2]

Option A: take 4  → earn 4, delete all 3s and 5s → [2] → take 2 → earn 2 → total 6 ✓
Option B: take 3  → earn 3, delete all 2s and 4s → []  → total 3
Option C: take 2  → earn 2, delete all 1s and 3s → [4] → take 4 → earn 4 → total 6 ✓

Answer: 6
```

**Example 2:**
```
nums = [2, 2, 3, 3, 3, 4]

Take all 3s → earn 3 × 3 = 9, deletes all 2s and 4s → total 9 ✓

Answer: 9
```

---

## Key Insight — Reduction to House Robber

Once you decide to take any copy of value `v`, you might as well take **all copies**
of `v` (they cost nothing extra to "earn").  So the total gain for choosing `v` is:

```
gain(v) = v × count(v)
```

The deletion rule says: if you choose `v`, you cannot choose `v-1` or `v+1`.
This is **exactly the House Robber adjacency constraint** applied to the sorted
list of distinct values.

**Transformation steps:**

1. Count the frequency of every value with a `Counter`.
2. Sort the distinct values.
3. Run the House Robber DP on `gain(v)` for each distinct value, treating two
   values as "adjacent" only when they differ by exactly 1.

---

## Recurrence

Let `vals` be the sorted distinct values and `gain(v) = v × count[v]`.

```
dp[i] = max(dp[i-1], dp[i-2] + gain(vals[i]))   if vals[i] == vals[i-1] + 1
dp[i] = dp[i-1] + gain(vals[i])                  otherwise (no conflict)
```

Base cases: `dp[-1] = 0`, `dp[-2] = 0`.

Space-optimised to two variables `prev` and `curr`.

---

## Walkthrough — `nums = [2, 2, 3, 3, 3, 4]`

```
count = {2: 2, 3: 3, 4: 1}
vals  = [2, 3, 4]
gain  = {2: 4, 3: 9, 4: 4}

Initial:  prev = 0, curr = 0

val=2 (first): no previous neighbour
    prev, curr = 0, 0 + 4 = 4

val=3: consecutive with 2 (3 == 2 + 1)
    prev, curr = 4, max(4, 0 + 9) = 9

val=4: consecutive with 3 (4 == 3 + 1)
    prev, curr = 9, max(9, 4 + 4) = 9

return curr = 9
```

---

## Walkthrough — `nums = [1, 1, 1, 2, 4, 4]`

```
count = {1: 3, 2: 1, 4: 2}
vals  = [1, 2, 4]
gain  = {1: 3, 2: 2, 4: 8}

Initial:  prev = 0, curr = 0

val=1 (first):
    prev, curr = 0, 3

val=2: consecutive with 1 (2 == 1 + 1)
    prev, curr = 3, max(3, 0 + 2) = 3

val=4: NOT consecutive with 2 (4 ≠ 2 + 1) — gap, no conflict
    prev, curr = 3, 3 + 8 = 11

return curr = 11
```

---

## Implementation

```python
from collections import Counter
from typing import List


def deleteAndEarn(nums: List[int]) -> int:
    count = Counter(nums)
    nums = sorted(count.keys())

    prev, curr = 0, 0

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1] + 1:
            prev, curr = curr, max(curr, prev + num * count[num])
        else:
            prev, curr = curr, curr + num * count[num]
    return curr
```

The `else` branch handles a gap between distinct values — since there is no
conflict, we simply accumulate the gain of the current value.

---

## Complexity

| Metric | Value          | Reason                                                     |
|--------|----------------|------------------------------------------------------------|
| Time   | O(n + k log k) | O(n) to count, O(k log k) to sort k distinct values        |
| Space  | O(k)           | Counter and sorted list of k distinct values               |

In the worst case `k = n` (all distinct), giving O(n log n) time overall.

---

## Edge Cases

| Input              | Output | Reason                                      |
|--------------------|--------|---------------------------------------------|
| `[1]`              | `1`    | Single element — always take it             |
| `[1, 2]`           | `2`    | Consecutive — pick the larger gain          |
| `[1, 3, 5]`        | `9`    | No consecutive values — take all            |
| `[2, 2, 3, 3, 3, 4]` | `9`  | Cluster of 3s dominates both neighbours     |
| `[1, 100]`         | `101`  | Large gap — both values are safe to take    |
