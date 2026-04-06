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
