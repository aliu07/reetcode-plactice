from typing import List


class Solution:
    """
    Intuition:
        Maintain a hash set. If we have a collision, then we know we
        encountered a duplicate.

    Runtime:
        O(n).

    Memory:
        O(n).
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False
