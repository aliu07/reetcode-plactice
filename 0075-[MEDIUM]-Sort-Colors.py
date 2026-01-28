from typing import List


class Solution:
    """
    Intuition:
        Count the frequency of each colour. Then pass through the array
        in-place and overwrite elements.

    Runtime:
        O(n) for 2 linear passes.

    Memory:
        O(1).
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0: 0, 1: 0, 2: 0}

        for n in nums:
            count[n] += 1

        ix = 0
        for _ in range(count[0]):
            nums[ix] = 0
            ix += 1

        for _ in range(count[1]):
            nums[ix] = 1
            ix += 1

        for _ in range(count[2]):
            nums[ix] = 2
            ix += 1
