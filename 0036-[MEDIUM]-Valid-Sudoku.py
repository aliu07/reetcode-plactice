from typing import List


class Solution:
    """
    Intuition:
        We can use hashing by row, column, and square (3x3 unit in the
        sudoku grid) to be able to perform fast lookups. The logic surrounding
        the squares requires some integer division math.

    Runtime:
        O(81) ~ O(1) since a sudoku is bounded as a 9x9 grid.

    Memory:
        Also O(1) since a sudoku is of a fixed size, meaning
        our hashsets have a defined upper bound.
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                if val in rows[i]:
                    return False
                else:
                    rows[i].add(val)

                if val in cols[j]:
                    return False
                else:
                    cols[j].add(val)

                if val in squares[i // 3][j // 3]:
                    return False
                else:
                    squares[i // 3][j // 3].add(val)

        return True
