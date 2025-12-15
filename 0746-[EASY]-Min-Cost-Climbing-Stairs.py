import math
from typing import List


class Solution1:
    """
    Intuition:
        Define base cases, then build dp array from bottom
        up.

        At the end, we can either take 1 step of 2 steps to
        reach top, so take min of last 2 elements.

    Runtime:
        O(n)

    Memory:
        O(n)
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [math.inf] * N
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, N):
            c1 = dp[i - 1] + cost[i]
            c2 = dp[i - 2] + cost[i]
            dp[i] = min(c1, c2)

        return min(dp[-1], dp[-2])


class Solution2:
    """
    Intuition:
        Same as Solution1.

    Runtime:
        O(n)

    Memory:
        O(1)
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        # at given index i
        # prev2 = lowest cost 2 steps down
        # prev1 = lowest cost 1 step down
        prev2, prev1 = cost[0], cost[1]

        for i in range(2, N):
            prev2, prev1 = prev1, min(prev2 + cost[i], prev1 + cost[i])

        return min(prev1, prev2)
