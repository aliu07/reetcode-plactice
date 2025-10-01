from typing import List


class Solution:
    """
    Intuition:
        After rotating the sorted array, there will be two distinct
        sorted partitions. We use a binary search approach while
        always comparing the mid-point value with the value at index
        r.

        If the value at mid is less than the value at r, we that the
        subarray between mid and r is sorted. As such, it can be the
        case that the value at mid is the minimum or that the minimum
        lies on the left, hence the update or r = mid.

        On the contrary, if the value at mid is greater than the one
        at r, then we know that the given segment is not sorted and
        that the partition wall or pivot lies somewhere in betwen.
        We know that the minimum element is the first element to the
        right of the pivot point, so we need to keep searching in that
        segment, hence l = mid + 1.

    Runtime:
        O(log n) since we are using a binary search approach.

    Memory:
        O(1) since we are only storing pointers.
    """

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # mid to r is sorted
            if nums[mid] < nums[r]:
                r = mid
            # mid to r is not sorted (i.e. partition wall lies somewhere in between)
            else:
                l = mid + 1

        return nums[l]
