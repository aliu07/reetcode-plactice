import heapq
from collections import defaultdict
from typing import List


class Solution1:
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


class Solution2:
    """
    Intuition:
        Use Prim's Algorithm. It relies on keeping track of connected
        points through a hash set and greedily taking the min-cost edge
        via a min-heap.

    Runtime:
        Building the adjacency list takes O(n^2) time.

        Each pair of points is processed at most once. The min-heap
        contains at most all pairs. Thus, pushing and popping from
        this min-heap takes at most O(log n^2) ~ O(log n). Since we
        have up to O(n^2) unique pairs, the total runtime to explore
        all points is O(n^2 * log n).

        Thus, total runtime is O(n^2 * log n).

    Memory:
        Adjacency list takes O(n^2) space.

        Visited set takes O(n) space.

        Min-heap takes at most O(n^2) space.

        Thus, O(n^2) overall space complexity.
    """

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # build adj list
        adj = defaultdict(list)
        for i in range(N):
            x1, y1 = points[i]

            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        res = 0
        visited = set()
        min_heap = [(0, 0)]
        while len(visited) < N:
            cost, i = heapq.heappop(min_heap)

            if i in visited:
                continue

            res += cost
            visited.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(min_heap, (nei_cost, nei))

        return res
