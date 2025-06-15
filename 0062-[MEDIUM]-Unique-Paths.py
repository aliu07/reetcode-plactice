import math

class Solution1:
    """
    Intuition:
        We need to take N steps to traverse the grid in total. K here represents
        the number of steps we need to take down. We can use the binomial theorem
        to compute the number of ways to choose K downward steps with N total.

    Runtime: O(m + n) bounded by the largest factorial computation (i.e. N = m + n - 2)

    Memory: O(1)

    Notes:
        This solution is the mathy solution. There exists a 2D DP approach too.
    """

    def uniquePaths(self, m: int, n: int) -> int:
        N = (m - 1) + (n - 1)
        K = (m - 1)
        return math.factorial(N) // (math.factorial(K) * math.factorial(N - K))



class Solution2:
    """
    Intuition:
        This problem satisfies the overlapping subproblem and optimal substructure
        properties of a DP problem. We can reuse solutions to smaller grids to
        solve larger grids and the number of unique paths (i.e. the optimal solution)
        to a smaller grid helps build the optimal solution to the larger grid.

        Our base case is a 1x1 grid where we only have 1 unique path. Since we are
        told we can only travel RIGHT or DOWN, we know that at each step, there are
        2 different options.

        Thus, we create a cache matrix where each cell's value represent the number
        of unique ways to reach that specific cell. Our base cases are the first row
        and left column as there is only one unique way to reach either of those cells.

        Then, for every other cell, we know that to reach it, we either came from above
        (traveling DOWN) or from the left (traveling RIGHT). Thus, we peek the adjacent
        cells up and to the left and sum their values.

    Runtime: O(m + n)

    Memory: O(m + n)

    Notes:
        Slightly less memory efficient than the math approach solution.
    """

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # Base case - first row
        for i in range(m):
            dp[i][0] = 1

        # Base case - first col
        for j in range(n):
            dp[0][j] = 1

        # DP steps
        for i in range(1, m):
            for j in range(1, n):
                numPaths = dp[i - 1][j] + dp[i][j - 1]
                dp[i][j] = numPaths

        return dp[-1][-1]
