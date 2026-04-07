# Dynamic Programming Mastery

A structured, 7-month journey through Dynamic Programming patterns — from Fibonacci foundations to Bitmask DP. Each problem is implemented in Python with a docstring, a full test suite, and a markdown breakdown that explains the approach step by step.

---

## Running Tests

```bash
# All tests
.venv/bin/pytest

# A specific problem
.venv/bin/pytest dynamic_programming/constant_transition/house_robber/test_house_robber.py -v
```

---

## 7-Month Learning Plan

### Stage 01 — Fibonacci Numbers Pattern `Month 1`

Master the foundation: `dp[i]` depends on a fixed number of previous states.

**Goal:** Solve Climbing Stairs, House Robber, and similar problems confidently.

**Key recurrence:**
```
dp[i] = f(dp[i-1], dp[i-2])
```

**Learning Resources:**

| Resource                                                                                                                                                                         | Type |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| [Aditya Verma — DP Playlist](https://www.youtube.com/watch?v=nqowUJzG-iM&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go) (start from intro, covers Fibonacci → Knapsack)                | YouTube |
| [Back To Back SWE — The Recursive Staircase (Top Down & Bottom Up DP)](https://www.youtube.com/watch?v=NFJ3m9a1oJQ)                                                              | YouTube |
| [Back To Back SWE — Total Ways To Decode A String](https://www.youtube.com/watch?v=YcJTyrG3bZs)                                                                                  | YouTube |
| [NeetCode - Decode Ways](https://www.youtube.com/watch?v=6aEyTjOwlJU)                                                                                                            | YouTube |
| [NeetCode - Min Cost Climbing Stairs](https://www.youtube.com/watch?v=ktmzAZWkEZ0)                                                                                                            | YouTube |
| [NeetCode - Delete and Earn](https://www.youtube.com/watch?v=7FCemBxvGw0)                                                                                                            | YouTube |
| [freeCodeCamp — Dynamic Programming Visual Course](https://www.youtube.com/watch?v=73r3KWiEvyk) (6 patterns, starts with Constant Transition)                                    | YouTube |
| [NeetCode 150 / 250](https://neetcode.io/practice) — 1-D Dynamic Programming section                                                                                             | Platform |
| [CP-Algorithms — Introduction to DP](https://cp-algorithms.com/dynamic_programming/intro-to-dp.html) — Fibonacci as foundation, memoization vs tabulation                        | Article |
| [AlgoMaster — 20 Patterns to Master DP](https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming) — pattern index with problem links                               | Article |
| [HackerEarth — Introduction to DP](https://hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/) — theory + practice problems | Article |

**Practice Problems:**

| Problem | Source | Difficulty | Key Idea |
|---------|--------|-----------|----------|
| ~~[Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)~~ | LeetCode 509 | Easy | Pure Fibonacci, memoize / tabulate |
| ~~[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)~~ | LeetCode 70 | Easy | dp[i] = dp[i-1] + dp[i-2] |
| [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | LeetCode 746 | Easy | Fibonacci + min choice |
| ~~[N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)~~ | LeetCode 1137 | Easy | 3-state Fibonacci |
| ~~[House Robber](https://leetcode.com/problems/house-robber/)~~ | LeetCode 198 | Medium | dp[i] = max(dp[i-1], dp[i-2]+nums[i]) |
| ~~[House Robber II](https://leetcode.com/problems/house-robber-ii/)~~ | LeetCode 213 | Medium | Circular → two linear subproblems |
| [Delete and Earn](https://leetcode.com/problems/delete-and-earn/) | LeetCode 740 | Medium | Reduce to House Robber |
| ~~[Decode Ways](https://leetcode.com/problems/decode-ways/)~~ | LeetCode 91 | Medium | Fibonacci with conditions |
| [Max Alternating Subsequence Sum](https://leetcode.com/problems/maximum-alternating-subsequence-sum/) | LeetCode 1911 | Medium | Two-state DP |
| ~~[Memoized Fibonacci](https://www.codewars.com/kata/529adbf7533b761c560004e5)~~ | Codewars 5kyu | Easy | Implement memoization |
| [The Millionth Fibonacci Kata](https://www.codewars.com/kata/53d40c1e2f13e331fc000c26) | Codewars 3kyu | Hard | Matrix exponentiation |
| [Fibonacci, Tribonacci and Friends](https://www.codewars.com/kata/556e0fccc392c527f20000c5) | Codewars 6kyu | Easy | Generalized k-bonacci |
| [Dice Combinations](https://cses.fi/problemset/task/1633) | CSES | Easy | Generalized staircase (6 choices) |
| [Fibonacci Numbers](https://cses.fi/problemset/task/1722) | CSES | Medium | Matrix exponentiation for large n |
| [Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a) | AtCoder DP | Easy | Fibonacci-like on heights |
| [Frog 2](https://atcoder.jp/contests/dp/tasks/dp_b) | AtCoder DP | Easy | Generalized k-step Frog |

**Daily rhythm:**
- 15 min — watch one video segment
- 15 min — write the recurrence, base case, and complexity
- 30 min — solve 1 problem (try alone for 20 min, then check)
- Weekly — re-solve 2 earlier problems without hints

---

### Stage 02 — 0/1 Knapsack `Month 2`

Understand the "include or exclude" decision framework.

**Goal:** Master Partition Equal Subset Sum, Target Sum, and their variants.

**Key recurrence:**
```
dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight[i]] + value[i])
```

**Learning Resources:**

| Resource                                                                                                                                           | Type |
|----------------------------------------------------------------------------------------------------------------------------------------------------|------|
| [Aditya Verma — Knapsack videos](https://www.youtube.com/watch?v=nqowUJzG-iM&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go) (videos 3–15 in the playlist) | YouTube |
| [Back To Back SWE — The 0/1 Knapsack Problem](https://www.youtube.com/watch?v=xCbYmUPvc2Q)                                                         | YouTube |
| [WilliamFiset — The 0/1 Knapsack Problem](https://www.youtube.com/watch?v=cJ21moQpofY)                                                                                       | YouTube |
| [NeetCode](https://neetcode.io/practice) — 1D & 2D DP sections                                                                                     | Platform |
| [CP-Algorithms — Knapsack](https://cp-algorithms.com/dynamic_programming/knapsack.html)                                                            | Article |

**Practice Problems:**

| Problem | Source | Difficulty |
|---------|--------|-----------|
| [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | LeetCode 416 | Medium |
| [Target Sum](https://leetcode.com/problems/target-sum/) | LeetCode 494 | Medium |
| [Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) | LeetCode 1049 | Medium |
| [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) | LeetCode 474 | Medium |
| [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | LeetCode 698 | Medium |
| [Book Shop](https://cses.fi/problemset/task/1158) | CSES | Medium |

**Daily rhythm:**
- 20 min — watch Aditya Verma's knapsack videos (1–2 per day)
- 40 min — solve 1 problem
- Weekly — re-solve 1–2 problems from Stage 1

---

### Stage 03 — Unbounded Knapsack `Month 3`

Transition from "use once" to "use unlimited times."

**Goal:** Master Coin Change and its variants.

**Key recurrence:**
```
dp[w] = min(dp[w], dp[w - coin] + 1)   # each coin usable many times
```

**Learning Resources:**

| Resource | Type |
|----------|------|
| [Back To Back SWE — The Change Making Problem (Fewest Coins)](https://www.youtube.com/watch?v=jgiZlGzXMBw) | YouTube |
| [Back To Back SWE — Total Unique Ways To Make Change](https://www.youtube.com/watch?v=DJ4a7cmjZY0) | YouTube |

**Practice Problems:**

| Problem | Source | Difficulty |
|---------|--------|-----------|
| [Coin Change](https://leetcode.com/problems/coin-change/) | LeetCode 322 | Medium |
| [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | LeetCode 518 | Medium |
| [Perfect Squares](https://leetcode.com/problems/perfect-squares/) | LeetCode 279 | Medium |
| [Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/) | LeetCode 983 | Medium |
| [Integer Break](https://leetcode.com/problems/integer-break/) | LeetCode 343 | Medium |
| [Minimizing Coins](https://cses.fi/problemset/task/1634) | CSES | Medium |
| [Coin Combinations I](https://cses.fi/problemset/task/1635) | CSES | Medium |
| [Coin Combinations II](https://cses.fi/problemset/task/1636) | CSES | Medium |

**Daily rhythm:**
- 20 min — continue Aditya Verma's unbounded knapsack videos
- 40 min — solve 1 problem; compare 0/1 vs unbounded recurrence
- Weekly — re-solve 1–2 problems from Stages 1–2

---

### Stage 04 — LCS & Subsequences `Month 4`

Master two-sequence DP.

**Goal:** Solve LCS, LIS, Edit Distance, and Distinct Subsequences.

**Key recurrence:**
```
dp[i][j] = dp[i-1][j-1] + 1            if s1[i] == s2[j]
dp[i][j] = max(dp[i-1][j], dp[i][j-1]) otherwise
```

**Learning Resources:**

| Resource | Type |
|----------|------|
| [Back To Back SWE — Longest Common Subsequence](https://www.youtube.com/watch?v=ASoaQq66foQ) | YouTube |
| [Back To Back SWE — Edit Distance (Levenshtein Distance)](https://www.youtube.com/watch?v=MiqoA-yF-0M) | YouTube |
| [Back To Back SWE — Longest Increasing Subsequence](https://www.youtube.com/watch?v=fV-TF4OvZpk) | YouTube |

**Practice Problems:**

| Problem | Source | Difficulty |
|---------|--------|-----------|
| [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | LeetCode 1143 | Medium |
| [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | LeetCode 300 | Medium |
| [Edit Distance](https://leetcode.com/problems/edit-distance/) | LeetCode 72 | Medium |
| [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | LeetCode 115 | Hard |
| [Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/) | LeetCode 1092 | Hard |
| [Interleaving String](https://leetcode.com/problems/interleaving-string/) | LeetCode 97 | Medium |
| [Edit Distance](https://cses.fi/problemset/task/1639) | CSES | Medium |

**Daily rhythm:**
- 15 min — watch NeetCode or Aditya Verma's LCS series
- 45 min — solve 1 problem (2D tables take longer — be patient)
- 10 min — explain solution out loud
- Weekly — re-solve 1–2 problems from previous stages

---

### Stage 05 — Palindromes `Month 5`

Apply subsequence and substring DP to palindrome problems, building on LCS.

**Goal:** Recognise palindrome structure in both substring and subsequence variants.

**Learning Resources:**

| Resource | Type |
|----------|------|
| [Back To Back SWE — Generate All Palindromic Decompositions](https://www.youtube.com/watch?v=4ykBXGbonlA) | YouTube |

**Practice Problems:**

| Problem | Source | Difficulty |
|---------|--------|-----------|
| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | LeetCode 5 | Medium |
| [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | LeetCode 647 | Medium |
| [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) | LeetCode 516 | Medium |
| [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) | LeetCode 132 | Hard |
| [Min Insertions to Make Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) | LeetCode 1312 | Hard |

---

### Stage 06 — Interval DP `Month 6`

Learn `dp[i][j]` over subarray intervals.

**Goal:** Handle hard interview problems like Burst Balloons.

**Key pattern:**
```
for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        for k in range(i, j):
            dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j] + cost)
```

**Learning Resources:**

| Resource | Type |
|----------|------|
| [WilliamFiset — Tiling dominoes](https://youtu.be/yn2jnmlepY8) | YouTube |
| [WilliamFiset — Tiling Dominoes and Trominoes](https://www.youtube.com/watch?v=CecjOo4Zo-g) | YouTube |
| [CP-Algorithms — Interval DP & Profile DP](https://cp-algorithms.com/dynamic_programming/profile-dynamics.html) | Article |

**Practice Problems:**

| Problem | Source | Difficulty |
|---------|--------|-----------|
| [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | LeetCode 312 | Hard |
| [Min Cost Tree From Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) | LeetCode 1130 | Medium |
| [Strange Printer](https://leetcode.com/problems/strange-printer/) | LeetCode 664 | Hard |
| [Min Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) | LeetCode 1039 | Medium |
| [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/) | LeetCode 790 | Medium |
| [Best Time to Buy & Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) | LeetCode 188 | Hard |

---

### Stage 07 — Bitmask DP `Month 7`

Represent subsets as bitmasks. Handle assignment, TSP-style, and state-compression problems.

**Goal:** Solve the "boss level" DP pattern.

**Key pattern:**
```
dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + cost[i][j])
```

**Learning Resources:**

| Resource | Type |
|----------|------|
| [WilliamFiset — Traveling Salesman Problem (DP + Graph Theory)](https://www.youtube.com/watch?v=cY4HiiFHO1o) | YouTube |
| [WilliamFiset — Floyd-Warshall All Pairs Shortest Path](https://www.youtube.com/watch?v=4NQ3HnhyNfQ) | YouTube |
| [AlgoMaster — Bitmasking DP Pattern](https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming) (section 17) | Article |
| Search "Bitmask DP" on [NeetCode](https://neetcode.io/practice) / Errichto channels for walkthroughs | YouTube |

**Practice Problems:**

| Problem | Source | Difficulty |
|---------|--------|-----------|
| [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | LeetCode 698 | Medium |
| [Min Work Sessions to Finish Tasks](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) | LeetCode 1986 | Medium |
| [Fair Distribution of Cookies](https://leetcode.com/problems/fair-distribution-of-cookies/) | LeetCode 2305 | Medium |
| [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | LeetCode 847 | Hard |
| [Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/) | LeetCode 943 | Hard |
| [Hamiltonian Flights](https://cses.fi/problemset/task/1690) | CSES | Hard |

**Daily rhythm (Stages 5–7):**
- 15 min — study the pattern theory
- 45–60 min — solve 1 problem
- 10 min — explain solution out loud (mock interview style)
- Weekly — re-solve 2 problems from any earlier stage

---

## General Advice

- **Spaced repetition:** Revisit 1–2 solved problems from earlier stages every week. DP patterns fade fast without practice.
- **Pattern recognition:** Take 5 random LeetCode problems per week and classify them (DP? Which sub-pattern?) without solving — just categorize.
- **Track your solve rate:** Note independent solves vs. hint-assisted vs. editorial. Aim for 70%+ independent by Stage 7.
- **Explain out loud:** From Stage 4 onward, narrate your approach before coding. Communication matters as much as the solution.
- **Write the recurrence first:** For every problem define the state, recurrence, base case, and complexity before touching code.
- **Mock interviews:** In the final month, do 2–3 timed sessions — random DP problem, 40-minute timer, explain and solve.
