# House Robber — Problem Breakdown

## Problem

You are a robber planning to rob houses along a street. Each house has a certain
amount of money. The only constraint is that **adjacent houses have a security
system** — robbing two adjacent houses triggers an alarm.

Given a list `nums` where `nums[i]` is the money at house `i`, return the
**maximum amount you can rob** without triggering the alarm.

**Example:**
```
nums = [2, 7, 9, 3, 1]

Options:
  rob houses 0, 2, 4  ->  2 + 9 + 1 = 12  ✓ (best)
  rob houses 1, 3     ->  7 + 3     = 10
  rob houses 0, 2     ->  2 + 9     = 11

Answer: 12
```

---

## Key Insight

At each house `i` you face exactly one binary choice:

| Choice     | Money gained            | Previous state required |
|------------|-------------------------|-------------------------|
| **Rob it** | `nums[i] + best(i - 2)` | Must skip house `i - 1` |
| **Skip it**| `best(i - 1)`           | Free to have robbed `i - 1` |

The optimal value at house `i` is:

```
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

Base cases: `dp[-1] = 0`, `dp[-2] = 0` (no houses yet → no money).

---

## Walkthrough — `nums = [2, 7, 9, 3, 1]`

We track two variables instead of a full array:
- `prev` — best result achievable up to two houses ago
- `curr` — best result achievable up to the previous house

```
Initial:  prev = 0, curr = 0

house 0 (val=2):  new_curr = max(curr=0, prev=0 + 2) = 2
                  prev, curr = 0, 2

house 1 (val=7):  new_curr = max(curr=2, prev=0 + 7) = 7
                  prev, curr = 2, 7

house 2 (val=9):  new_curr = max(curr=7, prev=2 + 9) = 11
                  prev, curr = 7, 11

house 3 (val=3):  new_curr = max(curr=11, prev=7 + 3) = 11
                  prev, curr = 11, 11

house 4 (val=1):  new_curr = max(curr=11, prev=11 + 1) = 12
                  prev, curr = 11, 12

return curr = 12
```

---

## Implementation

```python
def rob(nums: List[int]) -> int:
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr
```

The parallel assignment `prev, curr = curr, max(curr, prev + num)` is crucial —
it captures the old values of both variables before either is overwritten.

---

## Complexity

| Metric | Value | Reason                                      |
|--------|-------|---------------------------------------------|
| Time   | O(n)  | Single pass through the list                |
| Space  | O(1)  | Only two scalar variables, no DP table      |

---

## Edge Cases

| Input         | Output | Reason                              |
|---------------|--------|-------------------------------------|
| `[5]`         | `5`    | Only one house — always rob it      |
| `[2, 1]`      | `2`    | Two houses — pick the larger one    |
| `[10, 1, 1, 10]` | `20` | Rob both ends (not adjacent)    |
| `[0, 0, 0]`   | `0`    | Nothing to gain                     |
