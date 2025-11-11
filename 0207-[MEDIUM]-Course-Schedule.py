from collections import deque
from typing import List


class Solution:
    """
    Intuition:
        We can model courses as nodes of a graph. The idea is to topologically
        validate the dependency tree formed by the prerequisite relationships
        given to us.

        First, we need a way to traverse the graph. An adjacency list solves
        this. Then, we need a way to keep track of topological ordering. We
        can count the in-degree of each node to be able to identify courses
        who have no prerequisites and those that have one.

        We then traverse the graph starting at the ones with no prerequisites.
        At the end, we need to check if we were able to cover all course in
        such an ordering.

    Runtime:
        Let the number of courses be V and the size of prerequisites be E.

        Building the adj list and counting the in-degrees takes O(E).

        Iterative DFS to traverse the graph takes O(V + E).

        Overall, O(V + E) runtime.

    Memory:
        The adjacency list is of size O(E).

        The inDegree list is of size O(V).

        The deque data structure is at most O(V).

        The set is at most O(V).

        Overall, O(V + E) memory.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        # build adjacency list
        # and
        # count in-degree of each node
        for a, b in prerequisites:
            adj[b].append(a)
            inDegree[a] += 1

        q = deque()
        seen = set()

        # seed courses (don't have any prereqs)
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                q.append(i)

        # traverse dependency tree
        while q:
            course = q.pop()
            seen.add(course)

            for nei in adj[course]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)

        # check if we covered all courses
        return len(seen) == numCourses
