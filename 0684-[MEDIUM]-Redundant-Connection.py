from typing import List


class Solution:
    """
    Intuition:
        Originally, I had this idea of maintaining a set of "discovered"
        nodes and iterating over the edges. The nodes contained in the
        set was meant to represent connected nodes. Thus, if we encounter
        an edge that contained both nodes in the seen set, this would
        mean they are already connected and we would thus have found our
        redundant edge. However, this approach is flawed and you can
        think of many edge cases this does not cover.

        The point is, the idea behind it was correct. The implementation
        approach was wrong. Instead of a set, we use disjoint sets or
        union find. We build connected components as we iterate through
        the edges. If a union fails between two nodes, that means they
        are already connected and we have thus found our redundant edge.

    Runtime:
        Let V be the number of nodes and E be the number of edges.

        Initiating parent and rank arrays take O(V) time each.

        Each edge is processed once, leading to O(E) time. The runtime
        complexity of the union operation relies on the runtime of the
        find operation as it calls it twice. The find operation takes
        O(α(V)). The α represents the inverse Ackermann function. For
        practical purposes, it can be simplified to constant time.

        Thus, our overall runtime is O(V + (E * α(V))) or O(V + E) if
        we decide to simplify.

    Memory:
        The parent and rank arrays each take O(V) space.

        Thus, the overall memory complexity if O(V).
    """

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)  # nodes 1...N

        # N + 1 since nodes start at 1, so 1-indexed
        par = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        # union find methods

        # returns parent of given node
        def find(n):
            if n != par[n]:
                # set parent to root parent
                # path compression!
                par[n] = find(par[n])

            return par[n]

        # performs union of 2 nodes
        # returns True if union succeeds, False if already in same disjoint set
        def union(n1, n2):
            par1, par2 = find(n1), find(n2)
            if par1 == par2:
                return False

            if rank[par1] > rank[par2]:
                par[par2] = par1
                rank[par1] += rank[par2]
            else:
                par[par1] = par2
                rank[par2] += rank[par1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        # should never get here
