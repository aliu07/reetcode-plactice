from typing import List


class Solution:
    """
    Intuition:
        We traverse the grid until we hit an island. We then explore
        that island using DFS and propagate tombstones to prevent
        double counting.

    Runtime:
        We need to iterate through each cell -> O(M * N).

        Each cell processed at most once during dfs. O(1) time to
        leave a tombstone, but for M * N cells yields O(M * N).

        Overall O(M * N) runtime.

    Memory:
        Call stack depth is at most M * N. Thus, O(M * N) memory.

    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            # out of bounds
            if r < 0 or r >= M or c < 0 or c >= N:
                return 0

            # cell contains 0
            if grid[r][c] != 1:
                return 0

            # leave tombstone
            grid[r][c] = -1

            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return 1 + up + down + left + right

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)

        return res
