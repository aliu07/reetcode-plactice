from typing import List


class Solution:
    """
    Intuition:
        Notice that any number XOR'ed by itself yields 0. On top of that,
        Any number XOR'ed with 0 yields itself. Therefore, we can XOR every
        element in the array so that every element that appears twice
        cancels out and we are left with the single number at the end.

    Runtime:
        O(n) -> one pass

    Memory:
        O(1) -> need space for result, no extra space required
    """

    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(1, len(nums)):
            res ^= nums[i]

        return res
