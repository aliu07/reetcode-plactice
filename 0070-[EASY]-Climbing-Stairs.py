class Solution:
    """
    Intuition:
        This is just a disguised Fibonacci sequence problem.

    Runtime:
        O(n)

    Memory:
        O(1)
    """

    def climbStairs(self, n: int) -> int:
        # suppose we want to know how many ways to climb k stairs
        # n1 = how many ways to climb k - 1 stairs (since we can take 1 step)
        # n2 = how many ways to climb k - 2 stairs (since we can also take 2 steps)
        n1, n2 = 1, 1

        for i in range(n - 1):
            n1, n2 = n2, n1 + n2

        return n2
