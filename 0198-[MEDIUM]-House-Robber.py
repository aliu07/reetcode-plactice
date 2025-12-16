from typing import List


class Solution1:
    """
    Intuition:
        Decision to rob current house overlaps with sub-problem
        of robbing previous houses. We can either decide to rob
        or not to rob.

        At each house, we compute max between not robbing i.e.
        carrying over sum from previously adjacent house or
        skipping the previous house, robbing two houses down
        and the current one.

    Runtime:
        O(n).

    Memory:
        O(n).
    """

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        N = len(nums)

        if N == 1:
            return nums[0]

        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, N):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]


class Solution2:
    """
    Intuition:
        Same as Solution1.

    Runtime:
        O(n).

    Memory:
        O(1).
    """

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        N = len(nums)

        if N == 1:
            return nums[0]

        rob1, rob2 = nums[0], max(nums[0], nums[1])

        for i in range(2, N):
            rob1, rob2 = rob2, max(rob2, rob1 + nums[i])

        return rob2
