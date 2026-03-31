# Fibonacci Number — Problem Breakdown

## Problem
Given n, return the n-th Fibonacci number.

F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)

**Example:**
```
n = 6  ->  0, 1, 1, 2, 3, 5, 8  ->  8
```

---

## Approach 1: Top-Down (Memoization)

**Idea:**
Solve recursively, cache results to avoid recomputing the same subproblems.

**Recurrence:**
```
fib(n) = fib(n-1) + fib(n-2)
base cases: fib(0) = 0, fib(1) = 1
```

**Walkthrough for n=5:**
```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) = 1
│   │   │   └── fib(0) = 0
│   │   │   cache[2] = 1
│   │   └── fib(1) = 1      (cache hit)
│   │   cache[3] = 2
│   └── fib(2) = 1          (cache hit)
│   cache[4] = 3
└── fib(3) = 2              (cache hit)
cache[5] = 5
```

**Complexity:**
- Time: O(n) — each subproblem computed once
- Space: O(n) — cache + recursion call stack

---

## Approach 2: Bottom-Up (Tabulation)

**Idea:**
Build the answer iteratively from the base cases upward.
Only track the previous two values — no recursion needed.

**Walkthrough for n=6:**
```
prev, curr = 0, 1
step 1: prev, curr = 1, 1   (0+1)
step 2: prev, curr = 1, 2   (1+1)
step 3: prev, curr = 2, 3   (1+2)
step 4: prev, curr = 3, 5   (2+3)
step 5: prev, curr = 5, 8   (3+5)
return curr = 8
```

**Complexity:**
- Time: O(n) — single pass
- Space: O(1) — only two variables

---

## Comparison

| Approach   | Time | Space | Notes                    |
|------------|------|-------|--------------------------|
| Top-Down   | O(n) | O(n)  | Intuitive, recursive     |
| Bottom-Up  | O(n) | O(1)  | Optimal, iterative       |
