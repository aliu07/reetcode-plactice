from typing import List
from collections import deque


class Solution:
    """
    Intuition:
        We can use BFS/DFS to traverse all the nodes and edges. We just need to keep
        track of the parent of each node since the edges are undirected. Keeping track
        of the parent will allow us to append neighbouring nodes without appending the
        node we just came from (which would make us process it twice). This way, if
        we ever come back to a node twice, we know that there is a cycle and the graph
        is not a valid tree.

    Runtime:
        O(n + e) -> We process each node at most once. We also need a pass to build
        the adjacency list.

    Memory:
        O(n^2) -> The adjacency list will be O(n^2) in the worst case if all nodes are
        inter-connected. The seen hashset only takes O(n). Memory is thus bounded by
        O(n^2).
    """

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([(-1, 0)])
        seen = set()

        while q:
            parent, node = q.pop()

            if node in seen:
                return False
            else:
                seen.add(node)

            for nei in adj[node]:
                if nei != parent:
                    q.append((node, nei))

        return len(seen) == n
