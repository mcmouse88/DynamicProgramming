# House Robber II — Problem Breakdown

## Problem

You are a robber planning to rob houses arranged in a **circle**. Each house has
a certain amount of money. Adjacent houses have a security system — robbing two
adjacent houses triggers an alarm.

Because the houses are circular, **the first and last house are also adjacent**.

Given a list `nums` where `nums[i]` is the money at house `i`, return the
**maximum amount you can rob** without triggering the alarm.

**Example:**
```
nums = [2, 3, 2]

Options (circular — house 0 and house 2 are adjacent):
  rob house 0 only     ->  2
  rob house 1 only     ->  3  ✓ (best)
  rob house 2 only     ->  2
  rob houses 0 and 2   ->  NOT allowed (adjacent in the circle)

Answer: 3
```

---

## Key Insight

The circular constraint makes it impossible to rob **both** house `0` and house
`n - 1`.  That gives us exactly two non-overlapping linear sub-problems:

| Sub-problem | Houses included | Houses excluded |
|-------------|-----------------|-----------------|
| **A** — skip the last  | `nums[0 … n-2]` | `nums[n-1]`      |
| **B** — skip the first | `nums[1 … n-1]` | `nums[0]`        |

The answer is the maximum of the two classic House Robber results:

```
answer = max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

Each call to `rob_linear` solves the original (linear) House Robber problem:

```
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

---

## Walkthrough — `nums = [2, 3, 2]`

**Sub-problem A:** `nums[:-1]` = `[2, 3]`

```
Initial:  prev = 0, curr = 0

house 0 (val=2):  new_curr = max(0, 0 + 2) = 2
                  prev, curr = 0, 2

house 1 (val=3):  new_curr = max(2, 0 + 3) = 3
                  prev, curr = 2, 3

result A = 3
```

**Sub-problem B:** `nums[1:]` = `[3, 2]`

```
Initial:  prev = 0, curr = 0

house 1 (val=3):  new_curr = max(0, 0 + 3) = 3
                  prev, curr = 0, 3

house 2 (val=2):  new_curr = max(3, 0 + 2) = 3
                  prev, curr = 3, 3

result B = 3
```

```
answer = max(3, 3) = 3  ✓
```

---

## Walkthrough — `nums = [1, 2, 3, 1]`

**Sub-problem A:** `nums[:-1]` = `[1, 2, 3]`

```
Initial:  prev = 0, curr = 0

house 0 (val=1):  prev, curr = 0, 1
house 1 (val=2):  prev, curr = 1, 2
house 2 (val=3):  prev, curr = 2, max(2, 1+3) = 4

result A = 4
```

**Sub-problem B:** `nums[1:]` = `[2, 3, 1]`

```
Initial:  prev = 0, curr = 0

house 1 (val=2):  prev, curr = 0, 2
house 2 (val=3):  prev, curr = 2, 3
house 3 (val=1):  prev, curr = 3, max(3, 2+1) = 3

result B = 3
```

```
answer = max(4, 3) = 4  ✓
```

---

## Implementation

```python
def rob(nums: List[int]) -> int:
    if len(nums) < 2:
        return nums[0]

    def helper(arr: List[int]) -> int:
        prev, curr = 0, 0
        for num in arr:
            prev, curr = curr, max(curr, prev + num)
        return curr

    return max(helper(nums[:-1]), helper(nums[1:]))
```

The `helper` function is the standard O(1)-space House Robber solver.
We call it twice on the two linear sub-arrays and return the maximum.

---

## Complexity

| Metric | Value | Reason                                       |
|--------|-------|----------------------------------------------|
| Time   | O(n)  | Two linear passes through sub-arrays of size n-1 |
| Space  | O(1)  | Only two scalar variables per pass, no DP table  |

---

## Edge Cases

| Input             | Output | Reason                                           |
|-------------------|--------|--------------------------------------------------|
| `[5]`             | `5`    | Single house — always rob it                     |
| `[2, 1]`          | `2`    | Two houses (adjacent both ways) — pick the larger |
| `[2, 3, 2]`       | `3`    | Circular constraint blocks robbing both ends      |
| `[1, 2, 3, 1]`    | `4`    | Skip last: rob house 0 (1) + house 2 (3)          |
| `[0, 0, 0]`       | `0`    | Nothing to gain                                  |
