from typing import List


class Solution:
    """
    Intuition:
        We need to take the first element of the list no matter what. Then,
        the rest of the problem becomes finding the 2 smallest elements in
        the remainder of the array.

    Runtime:
        O(n * log n) since we have to sort the list.

    Memory:
        O(1).
    """

    def minimumCost(self, nums: List[int]) -> int:
        # need to take the first elmt no matter what
        res = nums[0]
        # remove 1st elmt from list, then sort it and find the 2 smallest elmts
        res += sum(sorted(nums[1:])[0:2])
        return res
