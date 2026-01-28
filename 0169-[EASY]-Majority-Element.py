from typing import List


class Solution1:
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


class Solution2:
    """
    Intuition:
        Instead of counting frequency, we can manage state via a counter.
        Since the majority element is guaranteed to appear more than n / 2
        (i.e. half) the time, we can use the candidate variable to track
        what we think will be the majority element. If the counter stays
        positive, the candidate remains. If it ever becomes 0, we need
        to change our candidate.

    Runtime:
        Still O(n).

    Memory:
        O(1).
    """

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for n in nums:
            if count == 0:
                candidate = n

            count += 1 if n == candidate else -1

        return candidate
