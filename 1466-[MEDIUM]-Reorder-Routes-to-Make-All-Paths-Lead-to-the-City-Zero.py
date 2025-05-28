from typing import List
from collections import deque

class Solution1:
    """
    Intuition:
        The key thing to notice is that the graph forms a network tree rooted at
        city 0. As such, our goal is to traverse the entire tree.

        The constraint, though, is that we are given a directed graph. To deal
        with this fact, we can introduct reverse edges to model each connection
        as bidirectional. To keep track of original edges, we will assign an
        extra bit. A value of 1 indicates the edge is in the original connections
        and a value of 0 indicates the edge is "artificially" introduced.

        We then traverse the tree using DFS and keep track of where we came from
        i.e. the parent. If the edge going from the parent (which radiates from
        city 0) to the current city is in the original connections, we know we
        have to flip its direction to make it point towards the root of city 0.

    Runtime:
        O(V + E) ~ O(V) where V is the number of cities
        V ~= E since we have a network tree i.e. n nodes and n - 1 edges.

    Memory:
        O(V) where V is the number of cities

    Notes:
        Intuition is absolutely correct, but runtime on Leetcode is a bit lackluster.
        We can rewrite some parts of the logic to optimize it.
    """

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {i: set() for i in range(n)}

        for u, v in connections:
            # 1 = original edge
            adj[u].add((v, 1))
            # 0 = artificial reverse edge
            adj[v].add((u, 0))

        # Number of edges that need to be flipped
        res = 0
        # DFS from city 0, encode as (city, parent)
        q = deque([(-1, 0)])
        seen = set([0])

        while q:
            parent, city = q.pop()

            for nei, dir in adj[city]:
                if nei not in seen:
                    # Taking an original edge that needs to be flipped
                    if dir == 1:
                        res += 1

                    q.append((city, nei))
                    seen.add(nei)

        return res
