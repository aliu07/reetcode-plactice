class Solution1:
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


class Solution2:
    """
    Intuition:
        A solution involving a hash set is trivial. Instead of relying
        on an additional set, what if we were to treat the input array
        as the hash set?

        Treat the input array like a hash set. Each value we encounter
        is the key (we subtract 1 since 0-indexed). For every key, we
        flip the sign of the value at that slot.

        Thus, if we hash to a value that is already negative, then we
        know that we have a duplicate and can therefore return it.

        Note that we return the absolute value since a previous key
        could alter the sign at a given slot which will only be encountered
        and detected later. Consider the example [3, 1, 3, 4, 2].

    Runtime:
        Still O(n).

    Memory:
        O(1) now.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            # ix is the equivalent of our hashed key
            ix = abs(n) - 1

            if nums[ix] < 0:
                return abs(n)

            nums[ix] *= -1
