from math import inf
from typing import List


class Solution:
    """
    Intuition:
        We binary-search a partition on the SHORTER array so that the total number of elements
        on the left side across both arrays is half of the combined length.

        For a candidate cut A[:midA+1] | A[midA+1:] in A, we choose B’s matching cut so that
        left sizes add to half: midB = half - midA - 2. When the largest left elements
        (maxLeftA, maxLeftB) are both ≤ the smallest right elements (minRightA, minRightB), the
        split is correct.

        The median is then either the min of the right-side mins (odd total) or the average
        of the max left and min right (even total). Using −inf/+inf handles edge cuts cleanly.

    Runtime:
        O(log(min(m, n))) — we only binary-search over the shorter array’s indices.

    Memory:
        O(1) — constant extra space; we only keep a few pointers and boundary values.
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2  # rename arrays to A and B for simplicity
        total = len(A) + len(B)
        half = total // 2

        # assign shortest array to A
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            # middle index for array A
            midA = (l + r) // 2
            # middle index for array B
            # subtract 2 since A and B are 0-indexed, so need to account for offset
            midB = half - midA - 2

            # rightmost element (i.e. maximum) in the left partition of A
            # (mid ptr included in left partition)
            maxLeftA = A[midA] if midA >= 0 else -inf
            # leftmost element (i.e. minimum) in the right partiton of A
            minRightA = A[midA + 1] if (midA + 1) < len(A) else inf
            # rightmost element (i.e. maximum) in the left partition of B
            maxLeftB = B[midB] if midB >= 0 else -inf
            # leftmost element (i.e. minimum) in the right partiton of B
            minRightB = B[midB + 1] if (midB + 1) < len(B) else inf

            # we found our median when the partitions' bounds align
            #
            # we know at this point that the lengths of the left partitions
            # summed up would yield half the total variables based on how
            # we computed midA and midB.
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if total % 2:
                    return min(minRightA, minRightB)
                else:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2

            # if max value in left partition of A violates property that it needs to be
            # smaller than minimum value in right partition of B...
            #
            # need to readjust partition in A
            if maxLeftA > minRightB:
                r = midA - 1
            else:
                l = midA + 1
