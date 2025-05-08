from typing import List
from collections import deque

class Solution:
    """
    Intuition:
        We init a queue with the initial entrance coordinates. Then, we use BFS
        to traverse the maze and return the nearest exit. If no exit is found,
        we return -1.

    Notes:
        This solution is not super polished. There definitely is a better way of
        writing it while keeping the main idea.

    Runtime: O(m * n) since each cell is processed at most once

    Memory:
        O(m * n) since the queue holds at most every cell in the maze. Think for
        example of a 1x1 grid.
    """

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = "x"
        q = deque([(entrance[0], entrance[1])])
        steps = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            for i in range(len(q)):
                i, j = q.popleft()

                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and steps > 0:
                    return steps

                for di, dj in dirs:
                    I, J = i + di, j + dj

                    if 0 <= I < m and 0 <= J < n and maze[I][J] == ".":
                        q.append((I, J))

                        # Leave tombstone
                        maze[I][J] = "x"

                        print("added", I, J)

            steps += 1

        return -1
