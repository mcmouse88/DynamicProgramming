# Decode Ways — Problem Breakdown

## Problem

A string of digits can be decoded into letters using the mapping:
`'1' → 'A'`, `'2' → 'B'`, …, `'26' → 'Z'`.

Given a string `s` of digits, return the **number of ways** to decode it.
A string starting with `'0'` or containing an isolated `'0'` that cannot pair with the preceding digit is invalid.

**Examples:**
```
s = "12"   ->  "AB" (1,2) or "L" (12)         ->  2
s = "226"  ->  "BZ" (2,26), "VF" (22,6), "BBF" (2,2,6)  ->  3
s = "06"   ->  invalid (leading zero)           ->  0
```

---

## Key Insight

At each position `i` you decide:

| Choice          | Condition                                           | Contribution   |
|-----------------|-----------------------------------------------------|----------------|
| Take 1 digit    | `s[i] != '0'`                                       | `ways(i + 1)`  |
| Take 2 digits   | `s[i] == '1'` or (`s[i] == '2'` and `s[i+1] in '0'-'6'`) | `ways(i + 2)`  |

This gives the recurrence:
```
ways(i) = ways(i+1)                          if s[i] != '0'
        + ways(i+2)                          if two-digit decode is valid
base case: ways(len(s)) = 1   (empty suffix — one way to decode nothing)
```

---

## Approach 1: Top-Down (Memoized DFS)

**Idea:** Recurse from index 0, cache results to avoid recomputation.

```python
def numDecodingsTopDown(s: str) -> int:
    memo = {len(s): 1}

    def dfs(i):
        if i in memo:
            return memo[i]
        if s[i] == '0':
            return 0
        res = dfs(i + 1)
        if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
            res += dfs(i + 2)
        memo[i] = res
        return res

    return dfs(0)
```

**Complexity:** Time O(n), Space O(n) — memo table + call stack.

---

## Approach 2: Bottom-Up (Tabulation)

**Idea:** Fill a DP table from right to left, avoiding recursion.

```python
def numDecodingsBottomUp(s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1

    for i in reversed(range(n)):
        if s[i] == '0':
            continue
        dp[i] = dp[i + 1]
        if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
            dp[i] += dp[i + 2]
    return dp[0]
```

**Complexity:** Time O(n), Space O(n) — DP array.

---

## Approach 3: Space-Optimised (Two Variables)

**Idea:** `dp[i]` only ever looks at `dp[i+1]` and `dp[i+2]`, so keep just two
scalars `curr` (=`dp[i+1]`) and `prev` (=`dp[i+2]`).

```python
def numDecodings(s: str) -> int:
    n = len(s)
    curr, prev = 1, 0

    for i in reversed(range(n)):
        ttl = 0
        if s[i] != '0':
            ttl = curr
        if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
            ttl += prev if i + 2 < n else 1
        prev, curr = curr, ttl
    return curr
```

**Complexity:** Time O(n), Space O(1).

---

## Walkthrough — `s = "226"`

Iterating right to left (`i = 2, 1, 0`):

```
Initial:  curr = 1 (base), prev = 0

i=2, s[2]='6':  ttl = curr = 1          (single digit valid)
                no two-digit (i+1 out of range)
                prev, curr = 1, 1

i=1, s[1]='2':  ttl = curr = 1          (single digit valid)
                two-digit: '26' → valid  ttl += prev = 1   ->  ttl = 2
                prev, curr = 1, 2

i=0, s[0]='2':  ttl = curr = 2          (single digit valid)
                two-digit: '22' → valid  ttl += prev = 1   ->  ttl = 3
                prev, curr = 2, 3

return curr = 3  ✓
```

---

## Complexity Summary

| Approach          | Time | Space |
|-------------------|------|-------|
| Top-Down (memo)   | O(n) | O(n)  |
| Bottom-Up (table) | O(n) | O(n)  |
| Space-Optimised   | O(n) | O(1)  |

---

## Edge Cases

| Input    | Output | Reason                                    |
|----------|--------|-------------------------------------------|
| `"0"`    | `0`    | Leading zero — no valid decode            |
| `"10"`   | `1`    | Only `"10" → J`; `"1","0"` is invalid     |
| `"100"`  | `0`    | `'0'` at index 2 cannot be decoded alone  |
| `"27"`   | `1`    | `"27"` > 26, so only `"B","G"` is valid   |
| `"1"`    | `1`    | Single digit always valid                 |
