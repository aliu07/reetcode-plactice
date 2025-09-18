from typing import List


class Solution:
    """
    Intuition:
        Since the ocean is on the right of the buildings, we simply start from
        the right side of the array i.e. from the end. We keep track of the
        tallest building encountered at each step to determine if subsequent
        buildings will have an ocean view.

        We need to reverse the list at the end since we iterate from right to left
        and the problem wants us to return indices in order.

    Notes:
        To reverse the list, I used [::-1], but a simple 2 pointer helper function
        coult have done the job too

    Runtime: O(n)

    Space: O(n) if you consider answer array, but O(1) auxiliary space
    """

    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []

        res = []
        maxHeight = 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > maxHeight:
                maxHeight = heights[i]
                res.append(i)

        return res[::-1]
