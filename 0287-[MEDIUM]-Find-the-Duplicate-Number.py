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


class Solution3:
    """
    Intuition:
        Now what if we are told that we cannot modify the array? We can
        use Floyd's Tortoise and Hare cycle detection algorithm.

        We have n + 1 slots for elements in the range [1, n]. By the
        pigeonhole principle, at least one number repeats. Here, we can
        think of each index as a node. The value at the node is the
        pointer to the next node. Thus, having an array with a duplicate
        element is analogous to having a linked list with a cycle.

        The first loop detects a the presence of a cycle. If there is
        one, the slow and fast pointers will eventually meet.

        The second loop finds the 'entry point' of the cycle i.e. the
        duplicate number.

    Runtime:
        The slow ptr in the first loop moves at 1 increment per step.
        Thus, runtime is O(n).

        The second loop, we restart slow2 at the head and it also moves
        at one increment per step. Thus, the runtime is also O(n).

        Overall, we have a O(n) runtime.

    Memory:
        O(1) since only need ptrs.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
