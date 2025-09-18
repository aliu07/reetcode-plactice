import heapq
from typing import List
from math import inf


class Solution1:
    """
    Intuition:
        Can't use sorting, so build a max-heap. Then, we pop k-1
        elements to get the kth largest element.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        for i in range(k - 1):
            heapq.heappop(heap)

        return -heap[0]


class Solution2:
    """
    Intuition:
        Same idea as solution 1, but written more elegantly.
        Just maintain a min-heap of size k instead of fitting
        all elements into the heap first and then finding the
        kth largest element.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


class Solution3:
    """
    Intuition:
        We store an array that counts the frequency of each element. The
        index represents the element and the value represents its respective
        frequency.

        We need to init the size of the array to (maxVal - minVal + 1). The +1
        is to account for the 0 value. We need at least maxVal number of slots.
        We need to also factor in the offset of minVal. This is because the
        input array can contain negative values.

        Consider if minVal is positive, then we only need maxVal - minVal + 1
        slots to hold all the numbers. If minVal is negative, then it expands
        the size of the array to account for potential negative values.

        Then, to find the kth largest number, we just iterate through the freq
        list and check the count at each index. If k drops below 0, that means
        we have found our kth largest element.

        We just need to keep in mind to offset the index where we're inserting
        at by minVal as well when building the frequency list. Also, we need
        to offset the result index.

    Notes:
        There exists another solution with similar runtime, but it is more
        esoteric.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxVal, minVal = -inf, inf

        for num in nums:
            if num > maxVal:
                maxVal = num

            if num < minVal:
                minVal = num

        freq = [0] * int(maxVal - minVal + 1)

        for num in nums:
            freq[int(num - minVal)] += 1

        for i in range(len(freq) - 1, -1, -1):
            k -= freq[i]

            if k <= 0:
                return int(i + minVal)

        # Should never reach this point
        return -1
