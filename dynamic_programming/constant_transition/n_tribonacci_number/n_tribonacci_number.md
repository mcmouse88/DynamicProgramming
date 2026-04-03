# N-th Tribonacci Number — Problem Breakdown

## Problem

The Tribonacci sequence is defined as:

T(0) = 0, T(1) = 1, T(2) = 1, T(n) = T(n-1) + T(n-2) + T(n-3)

Given n, return T(n).

**Example:**
```
n = 4  ->  0, 1, 1, 2, 4  ->  4
n = 25 ->  1389537
```

---

## Approach: Bottom-Up (Tabulation)

**Idea:**
Same as Fibonacci, but track three previous values instead of two.
Iterate from 3 to n, shifting the window of three states forward each step.

**Recurrence:**
```
T(n) = T(n-1) + T(n-2) + T(n-3)
base cases: T(0) = 0, T(1) = 1, T(2) = 1
```

**Walkthrough for n=6:**
```
first, second, third = 0, 1, 1

step 3: first, second, third = 1, 1, 0+1+1 = 2
step 4: first, second, third = 1, 2, 1+1+2 = 4
step 5: first, second, third = 2, 4, 1+2+4 = 7
step 6: first, second, third = 4, 7, 2+4+7 = 13

return third = 13
```

**Complexity:**
- Time: O(n) — single pass
- Space: O(1) — only three variables

---

## Connection to Fibonacci

| Sequence    | Recurrence                        | States tracked |
|-------------|-----------------------------------|----------------|
| Fibonacci   | F(n) = F(n-1) + F(n-2)           | 2              |
| Tribonacci  | T(n) = T(n-1) + T(n-2) + T(n-3) | 3              |

Tribonacci is a direct extension — add one more term and one more state variable. The same rolling-window trick applies: shift `(first, second, third)` instead of `(prev, curr)`.

---

## Edge Cases

| n | T(n) | Reason             |
|---|------|--------------------|
| 0 | 0    | Base case          |
| 1 | 1    | Base case          |
| 2 | 1    | Base case          |
| 3 | 2    | 0 + 1 + 1 = 2     |
