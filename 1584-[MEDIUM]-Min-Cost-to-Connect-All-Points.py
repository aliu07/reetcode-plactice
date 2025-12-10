from typing import List


class Solution:
    """
    Intuition:
        We can use a greedy approach here to always take the edge that
        costs the least. We first need to figure out the cost between
        every possible pair of points and then sort them based on cost
        i.e. distance.

        Then, we can use a disjoint set data structure to track our
        connected components and only tally the costs of edges that
        contribute to growing out connected graph.

        Inadvertently, we have implemented Kruskal's algorithm.

    Runtime:
        Creating all pairs combinations of points takes O(n^2) time.

        Sorting the pairs takes O(n^2 * log(n^2)) ~ O(n^2 * log n)
        time due to log laws.

        For practical purposes, we can consider that find() and union()
        are both constant time operations. Thus, iterating through all
        the pairs and performing union on them takes O(n^2) time.

        Overall, we have O(n^2 * log n) runtime.

    Memory:
        The pairs array takes O(n^2) space.

        The parent and rank arrays take O(n) each.

        Thus, we have O(n^2) space.
    """

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        pairs = []

        for i in range(len(points)):
            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                pairs.append((dist, i, j))

        pairs.sort()

        par = list(range(N))
        print(par)
        rank = [1] * N

        def find(n):
            if par[n] != n:
                par[n] = find(par[n])

            return par[n]

        def union(u, v):
            pu, pv = find(u), find(v)

            if pu == pv:
                return False

            # union by rank
            if rank[pu] > rank[pv]:
                par[pv] = pu
                rank[pu] += rank[pv]
            else:
                par[pu] = pv
                rank[pv] += rank[pu]

            return True

        res = 0
        for dist, u, v in pairs:
            if union(u, v):
                res += dist

        return res
