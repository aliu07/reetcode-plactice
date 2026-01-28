from typing import List


class Solution:
    """
    Intuition:
        We keep track of a running sum. This running sum also represents
        the subarray starting at 0.

        We also keep track of a hash map. This hash map represents the
        prefix sum at a given index. We don't really care about the
        index, more about the prefix sum which is why we track frequency
        of a prefix sum only.

        Then, we simply build the frequency hash map while running up our
        sum. We need to check for whenever the running sum equals the target
        or if there are prefix sums that yield the target.

    Runtime:
        O(n).

    Memory:
        O(n) for the hash map.
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        runningSum = 0
        res = 0

        for i in range(len(nums)):
            runningSum += nums[i]

            if runningSum == k:
                res += 1

            if runningSum - k in freq:
                res += freq[runningSum - k]

            freq[runningSum] = freq.get(runningSum, 0) + 1

        return res
