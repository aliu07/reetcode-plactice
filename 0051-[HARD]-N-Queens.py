from collections import deque
from typing import List


class Solution:
    """
    Intuition:
        Our approach relies on placing a queen at each cell in a row and
        then moving onto the next row. If the queen we place violates the
        rules of chess, then we backtrack to the previous row and have it
        place its queen in a different cell.

        We terminate once we have found a solution i.e. all queens have
        been placed.

    Runtime:
        Checking if the newly placed queen is safe:
            - O(n) to check all rows
            - O(2 * (n - 1)) ~ O(n) for diagonals
            - O(n) overall

        Copying the solution and appending it to res:
            - O(n^2) to copy since we need to process each cell
            - There are at most n solutions possible
            - Overall O(n * n^2)

        DFS:
            - We have n rows
            - We can choose among n - q cells in our given row where q
              is the number of queens we have placed so far
            - Overall O(n!)

        The algorithm is either exploring or copying the solution, so
        the overall runtime is O(n * n!) + O(n * n^2) which is bounded
        by O(n!).

    Memory:
        O(n^2) for the board.

        O(2 * (n - 1)) ~ O(n) for the deque.

        Total O(n^2) memory.
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        # we place queens by row, so only need to check
        # cols and diagonals
        def queenIsSafe(row, col):
            for r in range(n):
                if r != row and board[r][col] == "Q":
                    return False

            q = deque(
                [(row, col, (-1, -1)), (row, col, (-1, 1)), (row, col, (1, 1)), (row, col, (1, -1))]
            )

            while q:
                r, c, (dr, dc) = q.pop()

                # in bounds
                if 0 <= r + dr < n and 0 <= c + dc < n:
                    # check if cell has queen
                    if board[r + dr][c + dc] == "Q":
                        return False

                    # keep exploring
                    q.append((r + dr, c + dc, (dr, dc)))

            return True

        def dfs(currRow):
            if currRow == n:
                soln = ["".join(r) for r in board]
                res.append(soln)
                return

            for col in range(n):
                board[currRow][col] = "Q"  # place queen

                # check if newly placed queen is safe
                if queenIsSafe(currRow, col):
                    dfs(currRow + 1)

                board[currRow][col] = "."  # pick up queen

        dfs(0)
        return res
