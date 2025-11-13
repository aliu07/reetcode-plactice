from collections import deque
from typing import List


class Solution:
    """
    Intuition:
        Same as Course Schedule problem, but we need to build the ordering
        of courses in an array. Topological sort problem, but need to return
        ordering.

    Runtime:
        Let V be the number of courses and E be the number of prerequisite
        relations (edges).

        Computing the adjacency list and in degrees list takes O(E).

        Performing DFS takes O(V + E).

        Overall, O(V + E) time.

    Memory:
        Let V be the number of courses and E be the number of prerequisite
        relations (edges).

        Adjacency list takes size O(V + E) since we need to store an entry
        for each course and each entry scales with respect to the number of
        prerequisites.

        The deque takes up to O(V) space. Same for the result array.

        Overall, O(V + E) memory complexity.
    """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adj list
        # and in degree map
        adj = [[] for _ in range(numCourses)]
        inDegrees = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            inDegrees[a] += 1

        # dfs
        q = deque()
        res = []

        for course in range(numCourses):
            if inDegrees[course] == 0:
                q.append(course)

        while q:
            course = q.pop()
            res.append(course)

            for nei in adj[course]:
                inDegrees[nei] -= 1

                if inDegrees[nei] == 0:
                    q.append(nei)

        return res if len(res) == numCourses else []
