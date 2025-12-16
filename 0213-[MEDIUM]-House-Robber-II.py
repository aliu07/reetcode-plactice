from typing import List


class Solution:
    """
    Intuition:
        We need to ensure that the first are last houses are not both robbed
        considering they are adjacent now. We can guarantee exclusion by
        robbing two subsets of houses. The first subset exludes the first
        house to ensure we do not rob it. The second subset excludes the
        last house. As such, we can see the max amount in each scenario and
        pick the largest.

        We can take the space-optimized soln to House Robber to construct
        the following solution.

    Runtime:
        O(n).

    Memory:
        O(1).
    """

    def rob(self, nums: List[int]) -> int:
        # if nums only has 1 elmt, splicing it will give empty arrs
        # so just return the only elmt
        if len(nums) == 1:
            return nums[0]

        without_first_house = self.helper(nums[1:])
        without_last_house = self.helper(nums[:-1])
        return max(without_first_house, without_last_house)

    def helper(self, houses):
        if not houses:
            return 0

        N = len(houses)

        if N == 1:
            return houses[0]

        rob1, rob2 = houses[0], max(houses[0], houses[1])
        for i in range(2, N):
            rob1, rob2 = rob2, max(rob2, rob1 + houses[i])

        return rob2
