from math import inf
from typing import List


class Solution:
    """
    Intuition:
        We maintain a dynamic sliding window. We increment the right ptr
        as long as our sum is increasing. Whenever our sum dips below
        0, we adjust our left ptr and the current sum of the window
        accordingly.

    Runtime:
        O(n). Linear sliding window solution.

    Memory:
        O(1).
    """

    def maxSubArray(self, nums: List[int]) -> int:
        curr, res = 0, -inf
        l, r = 0, 0

        while r < len(nums):
            while curr < 0:
                curr -= nums[l]
                l += 1

            curr += nums[r]

            if curr > res:
                res = curr

            r += 1

        return res
