from typing import List


class Solution:
    """
    Intuition:
        Accelerate lookups by hasing each array into a hashset.

    Runtime: O(n)

    Memory: O(n)
    """

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        ans = [
            [elmt for elmt in set1 if elmt not in set2],
            [elmt for elmt in set2 if elmt not in set1],
        ]

        return ans
