from typing import List


class Solution:
    """
    Intuition:
        The only way for a region of O's to not be enclosed is if
        it is not surrounded on all sides by X's.

        This observation is equivalent to saying that a region is
        not surrounded if it is reachable from an O on the border
        of the board.

        As such, we can use DFS or BFS to traverse each O-cell on
        the board's boarder and find all reachable O's.

        The ones that are reachable will be marked with a tombstone.
        Then, we use a second pass to change those that were reachable
        back to O's while turning the unreachable ones to X's.

    Runtime:
        Exploring all cells reachable from border O's takes O(m * n).

        Second pass to update tombstones and surroudned regions takes
        O(m * n).

        Overall O(m * n) runtime.

    Memory:
        Recursion stack of DFS can reach up to O(m * n).

        Therefore, O(m * n) memory complexity.
    """

    def solve(self, board: List[List[str]]) -> None:
        M, N = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            # leave tombstone
            board[r][c] = "#"

            # keep exploring
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                # in bounds and is O
                if 0 <= nr < M and 0 <= nc < N and board[nr][nc] == "O":
                    dfs(nr, nc)

        # explore border O's
        for r in range(M):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][N - 1] == "O":
                dfs(r, N - 1)

        for c in range(N):
            if board[0][c] == "O":
                dfs(0, c)
            if board[M - 1][c] == "O":
                dfs(M - 1, c)

        # check board and modify in place
        # if cell is still O, then we know it is unreachable and surrounded
        # if cell is '#', then it is reachable from a border O and not surrounded
        for r in range(M):
            for c in range(N):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
