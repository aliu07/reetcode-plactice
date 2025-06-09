class Solution:
    """
    Intuition:
        Build a bottom up dp table to perform lookups. We use previously
        solved problem solutions to solve the bigger problem.

    Runtime:
        O(n)

    Memory:
        O(n) to store the dp array.
    """

    def tribonacci(self, n: int) -> int:
        BASE_CASES = {0: 0, 1: 1, 2: 1}

        if n in BASE_CASES:
            return BASE_CASES[n]

        dp = [0, 1, 1] + [0 for _ in range(3, n + 1)]

        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

        return dp[-1]
