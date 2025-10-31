from collections import deque
from typing import List


class Solution1:
    """
    Intuition:
        We iterate through the grid. When we hit an island, we
        increment our counter and propagate tombstones to avoid
        hitting it again and double counting it.

        This solution uses an iterate BFS approach.

    Runtime:
        We have M * N cells in our matrix.

        Each cell is processed with a tombstone at most once, so
        we have O(M * N).

        Overall we have O(2 * (M * N)) which simplifies to O(M * N).

    Memory:
        Our deque holds at most all cells of the matrix. Thus,
        we have a worst case space complexity of O(M * N).
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        M, N = len(grid), len(grid[0])

        for r in range(M):
            for c in range(N):
                if grid[r][c] == "1":
                    islands += 1

                    # bfs
                    q = deque([(r, c)])
                    while q:
                        for _ in range(len(q)):
                            row, col = q.popleft()

                            if row < 0 or row >= M or col < 0 or col >= N:
                                continue

                            if grid[row][col] != "1":
                                continue

                            grid[row][col] = "."

                            q.append((row + 1, col))
                            q.append((row - 1, col))
                            q.append((row, col + 1))
                            q.append((row, col - 1))

        return islands


class Solution2:
    """
    Intuition:
        Same as Solution1. Instead, we use a recursive DFS
        approach.

    Runtime:
        Same as Solution1.

    Memory:
        Same as Solution1.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        M, N = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= M or c < 0 or c >= N:
                return

            if grid[r][c] != "1":
                return

            grid[r][c] = "."
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(M):
            for c in range(N):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands
