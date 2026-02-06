from typing import List


class Solution:
    """
    Intuition:
        Use modulo to prevent out of bounds.

    Runtime:
        O(n).

    Memory:
        O(1) auxiliary space.
    """

    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []

        for i, n in enumerate(nums):
            if n == 0:
                res.append(n)
            else:
                res.append(nums[(i + n) % N])

        return res
