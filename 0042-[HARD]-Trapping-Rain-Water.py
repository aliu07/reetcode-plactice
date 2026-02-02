from typing import List


class Solution:
    """
    Intuition:
        This is the optimized 2 ptr approach. We keep track of the max
        heights on each side to be able to calculate retained water at
        each step.

        At each step, we compare the height at each pointer. The side
        with the smaller height will be the limiting factor, so we dom
        not even need to consult the opposite side to calculate the
        retained volume.

    Runtime:
        O(n).

    Memory:
        O(1).
    """

    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[-1]
        res = 0

        while l <= r:
            if height[l] < height[r]:
                maxL = max(maxL, height[l])
                res += maxL - height[l]
                l += 1
            else:
                maxR = max(maxR, height[r])
                res += maxR - height[r]
                r -= 1

        return res
