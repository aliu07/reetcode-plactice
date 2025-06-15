from typing import List

class Solution:
    """
    Intuition:
        This problem essentially presents a binary search problem among 2 partitions. Since
        the input array might be rotated, our invariant is that we have 2 distinct partitions
        where the elements are sorted.

        Therefore, we simply check if the middle pointer belongs to the left or right partition.
        The way we check this is to see if the sorted property is maintained.

        If the middle pointer belongs to the left partition, we check the target against both
        ends. If the target value is greater than the mid pointer, then it must be in the
        right partition. Similarly, if the target value is less than the left pointer, we know
        it must be in the right partition since the array is possibly rotated.

        A similar logic applies for if the mid pointer belongs to the right partition.

    Runtime:
        O(log n)

    Memory:
        O(1)

    Notes:
        Writing a linear time solution is trivial
    """

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # If mid ptr belongs to left partition
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # If mid ptr belongs to right partition
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
