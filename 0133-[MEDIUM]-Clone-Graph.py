from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution1:
    """
    Intuition:
        We can store a map where the original node is the key
        and the cloned node is the value.

        We use DFS to traversse the graph and build each node's
        clone while also recursively cloning its neighbours and
        adding them to the neighbors list of the current node.

    Runtime:
        We explore each node and process it once, leading to
        O(V).

        For each node, we also need to process all of its
        neighbours which is O(E).

        Overall O(V + E) runtime.

    Memory:
        Let V be the number of vertices and E the number of
        edges.

        Need map to store each node's clone -> O(V).

        Recursive call stack can span at most entire graph.
        Thus, O(V).

        Overall O(V).

    """

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        cloneMap = {}

        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]

            clone = Node(node.val)
            cloneMap[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node) if node else None


class Solution2:
    """
    Intuition:
        Same as Solution1. Instead, we use iterative BFS approach.

    Runtime:
        Same as Solution1.

    Memory:
        Same as Solution1.
    """

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        cloneMap = {}
        cloneMap[node] = Node(node.val)

        q = deque([node])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                clone = cloneMap[curr]

                for nei in curr.neighbors:
                    if nei not in cloneMap:
                        cloneMap[nei] = Node(nei.val)
                        q.append(nei)

                    clone.neighbors.append(cloneMap[nei])

        return cloneMap[node]
