from typing import List

class Solution:
    """
    Intuition:
        Perform 2 binary search operations. The first one will be to find
        the index of the row potentially containing our target value. The
        second will be to search within that row to see if the value is
        present.

    Runtime:
        O(log M + log N) becomes O(log(M * N)) by log rules.

    Memory:
        O(1)
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])

        # Find row
        l, r = 0, M - 1

        while l < r:
            mid = (l + r) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l = mid
                break

            if target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        # Row potentially containing target will be at 'l' ptr
        row = matrix[l]

        # Find col
        l, r = 0, N - 1

        while l < r:
            mid = (l + r) // 2

            if row[mid] == target:
                return True

            if target < row[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return row[l] == target
