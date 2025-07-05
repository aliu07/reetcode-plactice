from typing import List

class Solution:
    """
    Intuition:
        We define base cases and buid the subsequent rows using these
        base cases. Note that the first and last element of each row
        in the triangle is always 1.

    Runtime:
        O(N ^ 2) since notice that the nth row has n elements. Here,
        N represents numRows.

    Memory:
        O(N ^ 2) as well where N is the value of numRows.
    """


    def generate(self, numRows: int) -> List[List[int]]:
        # Base cases
        triangle = [[1], [1, 1]]

        if numRows <= 2:
            return triangle[:numRows]

        while len(triangle) < numRows:
            newRow = [1]
            prevRow = triangle[-1]

            for i in range(len(prevRow) - 1):
                newRow.append(prevRow[i] + prevRow[i + 1])

            newRow.append(1)
            triangle.append(newRow)

        return triangle
