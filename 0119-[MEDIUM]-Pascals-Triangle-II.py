from typing import List


class Solution:
    """
    Intuition:
        We only ever need the previous row to build the next row. As
        such, we only need to keep track of a singular row at each
        iteration instaed of storing all previous rows in a hashset.

    Runtime:
        O(N ^ 2) where N = rowIndex. The outer loop requires rowIndex
        iterations. On the rowIndex'th row, we need rowIndex number of
        elements.

    Memory:
        O(N) where N = rowIndex since we are only tracking a singular
        current row at a time.
    """

    def getRow(self, rowIndex: int) -> List[int]:
        curr = [1]

        for _ in range(rowIndex):
            prev = curr
            curr = [1]

            for j in range(len(prev) - 1):
                curr.append(prev[j] + prev[j + 1])

            curr.append(1)

        return curr
