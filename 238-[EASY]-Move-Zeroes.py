from typing import List

class Solution:
    """
    Intuition:
        Since we need to move the elements in place, we cannot allocate more
        memory for another array. Thus, the intuition behind solving this
        problem relies on using 2 ptrs. The left one will track the next insert
        position. The right one will be used to traverse the array.

        If we encounter a 0, we increment the right pointer and continue to the
        next iteration. If we encounter a non-zero element, we can insert it at
        the left pointer.

        The left ptr here represents the next immediate position where we would
        insert a non-zero element. After the right pointer reaches the end, we
        populate the remainder of the left array with 0's.

    Runtime:
        O(n) since we need to iterate through the entire array.

    Memory:
        O(1) since we shift elements in place.
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0

        while r < len(nums):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1

            r += 1

        while l < len(nums):
            nums[l] = 0
            l += 1
