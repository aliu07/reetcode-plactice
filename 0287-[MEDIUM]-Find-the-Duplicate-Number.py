class Solution:
    """
    Intuition:
        Use a hash set to keep track of seen numbers. Return
        upon collision. This solution is trivial.

    Runtime:
        O(n) -> one pass.

    Memory:
        O(n) for the hash set.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for n in nums:
            if n in seen:
                return n

            seen.add(n)
