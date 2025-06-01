from typing import List

class Solution:
    """
    Intuition:
        Rather than brute forcing, we can store number in a hashmap and
        simply perform a lookup for subsequent numbers to see if the
        difference between the target number and the current number is
        contained within the hashmap

    Runtime:
        O(n) where n is the number of elements in the input array

    Memory:
        O(n) where n is the number of elements in the input array

    Notes:
        We need to return the indices in order. Since we iterate from left
        to right, we know that if target - num is in the map, then the index
        associated will be smaller by default.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            if target - num in map:
                return [map[target - num], i]

            map[num] = i

        # Should never get here
        return [-1, -1]
