from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Intuition:
            Start from the end of each array since free space in nums1 is
            allocated at the end (where all the 0's are). Similar solution
            structure to merge 2 sorted linked lists.
        """
        ix = m + n - 1

        while m > 0 and n > 0:
            num1, num2 = nums1[m - 1], nums2[n - 1]

            if num1 >= num2:
                nums1[ix] = num1
                m -= 1
            else:
                nums1[ix] = num2
                n -= 1

            ix -= 1

        while m > 0:
            num = nums1[m - 1]
            nums1[ix] = num
            m -= 1
            ix -= 1

        while n > 0:
            num = nums2[n - 1]
            nums1[ix] = num
            n -= 1
            ix -= 1
