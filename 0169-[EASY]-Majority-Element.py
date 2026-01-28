from typing import List


class Solution:
    """
    Intuition:
        Keep track of frequency, return the number who appears
        more than n / 2 times.

    Runtime:
        O(n).

    Memory:
        O(n) for the hash map.
    """

    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

            if freq[n] > (len(nums) / 2):
                return n

        # should never get here
        return -1
