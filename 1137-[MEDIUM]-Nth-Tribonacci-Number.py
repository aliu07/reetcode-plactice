class Solution1:
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



class Solution2:
    """
    Intuition:
        We can remove the dp array by noticing that we only ever need the 3
        previous numbers in the sequence. Therefore, we can store them in
        separate variables and update them upon each iteration.

    Runtime:
        Still O(n)

    Memory:
        O(1) now since we removed the need for a dp cache.
    """
    def tribonacci(self, n: int) -> int:
        # Base cases
        t0, t1, t2 = 0, 1, 1

        if n == 0:
            return t0
        elif n == 1:
            return t1
        elif n == 2:
            return t2

        for i in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t2
