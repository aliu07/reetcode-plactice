from collections import deque
from math import inf
from typing import List


class Solution1:
    """
    Intuition:
        Instead of starting from the middle and checking if each cell can
        reach both oceans, we simply compute the reachability starting from
        each respective ocean and then compute the final result by taking
        taking the overlap from both Atlantic and Pacific matrices.

    Runtime:
        O(m * n) -> Need to process each cell once.

    Memory:
        O(m * n) -> Store boolean results in equal M x N matrices.

    """

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Constants
        M, N = len(heights), len(heights[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Process Atlantic
        atlantic = [[False] * N for _ in range(M)]
        init = []

        for r in range(M):
            init.append((heights[r][N - 1], r, N - 1))

        for c in range(N):
            init.append((heights[M - 1][c], M - 1, c))

        q = deque(init)
        while q:
            height, row, col = q.pop()
            atlantic[row][col] = True

            for dr, dc in dirs:
                new_r, new_c = row + dr, col + dc

                if (
                    0 <= new_r < M
                    and 0 <= new_c < N
                    and height <= heights[new_r][new_c]
                    and not atlantic[new_r][new_c]
                ):
                    q.append((heights[new_r][new_c], new_r, new_c))

        # Process Pacific
        pacific = [[False] * N for _ in range(M)]
        init = []

        for r in range(M):
            init.append((heights[r][0], r, 0))

        for c in range(N):
            init.append((heights[0][c], 0, c))

        q = deque(init)
        while q:
            height, row, col = q.pop()
            pacific[row][col] = True

            for dr, dc in dirs:
                new_r, new_c = row + dr, col + dc

                if (
                    0 <= new_r < M
                    and 0 <= new_c < N
                    and height <= heights[new_r][new_c]
                    and not pacific[new_r][new_c]
                ):
                    q.append((heights[new_r][new_c], new_r, new_c))

        # Compute res
        res = []
        for r in range(M):
            for c in range(N):
                if atlantic[r][c] and pacific[r][c]:
                    res.append([r, c])

        return res


class Solution2:
    """
    Intuition:
        Same as Solution1. Instead of processing Atlantic, then
        Pacific in a sequential manner, we can process both in
        the same loop to save a tiny bit of runtime.

    Runtime:
        Same as Solution1.

    Memory:
        Same as Solution1.
    """

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        pacific = [[False] * N for _ in range(M)]
        atlantic = [[False] * N for _ in range(M)]
        pacQ = deque()
        atlQ = deque()

        # init qs
        for r in range(M):
            pacQ.append((r, -1, -inf))
            atlQ.append((r, N, -inf))
        for c in range(N):
            pacQ.append((-1, c, -inf))
            atlQ.append((M, c, -inf))

        # bfs on both at same time
        while pacQ or atlQ:
            for _ in range(len(pacQ)):
                r, c, h = pacQ.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < M and 0 <= nc < N and not pacific[nr][nc] and heights[nr][nc] >= h:
                        pacific[nr][nc] = True
                        pacQ.append((nr, nc, heights[nr][nc]))

            for _ in range(len(atlQ)):
                r, c, h = atlQ.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < M
                        and 0 <= nc < N
                        and not atlantic[nr][nc]
                        and heights[nr][nc] >= h
                    ):
                        atlantic[nr][nc] = True
                        atlQ.append((nr, nc, heights[nr][nc]))

        res = []
        for r in range(M):
            for c in range(N):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])

        return res
