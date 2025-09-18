from typing import List


class Solution:
    """
    Intuition:
        Find kid with most candies with first pass. Then, for each kid, we compare
        the candies they have + the amount of extra candies and see if it exceeds the
        max previously found.

    Runtime: O(n)

    Memory: O(n), but O(1) auxiliary
    """

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0

        for amt in candies:
            maxCandies = max(maxCandies, amt)

        res = [False] * len(candies)

        for i in range(len(res)):
            if candies[i] + extraCandies >= maxCandies:
                res[i] = True

        return res
