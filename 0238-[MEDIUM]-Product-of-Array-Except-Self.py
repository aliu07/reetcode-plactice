from typing import List


class Solution:
    """
    Intuition:
        We perform 2 linear passes, one forward and one backward. With
        each pass, we maintain an accumulator variable.

        On the forward pass, the accumulator represents the product of
        all elements to the left of a given cell.

        On the backward pass, the accumulator represents the product of
        all elements to the right of a given cell.

    Runtime: O(n)

    Memory: O(n) in total or O(1) auxiliary (excluding result array)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        accum = 1
        for i in range(n):
            res[i] *= accum
            accum *= nums[i]

        accum = 1
        for i in range(n - 1, -1, -1):
            res[i] *= accum
            accum *= nums[i]

        return res
