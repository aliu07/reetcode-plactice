import heapq
from collections import deque
from math import inf
from typing import List


class Solution1:
    """
    Intuition:
        We start by building an adjancency list of our edges. Then, we
        use DFS to traverse the graph and compute the minimum times to
        reach every other node from k, maintaining a look-up table to do
        so. Finally, we take the largest time in the table and return it
        as our result.

    Runtime:
        Let E be the number of edges and V be the number of nodes.

        Building the adjacency list takes O(E) time.

        Performing DFS does not take the usual O(V + E) time. The current
        implementation does not guarantee that each node's distance improves
        only once. DFS can discover "heavier paths" first and then find
        shorter ones. When this happens, we incur the cost of re-exploring
        all outgoing edges of the node which takes at most O(E) time. Each
        node's distance can improve at most V times (we come from a
        different node each time).

        Finding the largest delay in the times array takes O(V) time.

        Overall, O(V * E) time.

    Memory:
        The adjacency list takes O(E) space.

        The DFS queue takes at most O(E) space (all outgoing edges
        present).

        The times array takes O(V) space.

        Thus, overall memory complexity of O(V + E).
    """

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adj list with weights/delays
        adj = [[] for _ in range(n + 1)]
        for u, v, delay in times:
            adj[u].append((v, delay))

        # init DFS
        q = deque([(k, 0)])
        # keep track of min time to reach each node from k
        times = [inf for _ in range(n + 1)]
        times[0] = 0  # index 0 is tombstone since nodes are 1-indexed

        # perform DFS
        while q:
            node, time = q.pop()

            if time < times[node]:
                times[node] = time

                # only keep exploring if it's worth it
                # i.e. current time was a minimum
                for nei, delay in adj[node]:
                    q.append((nei, time + delay))

        # compute result
        res = max(times)
        return res if res != inf else -1


class Solution2:
    """
    Intuition:
        Instead of relaxing edges multiple times (i.e. finding a better
        path multiple times), we can guarantee that every edge only gets
        relaxed once by using a min heap instead of a deque (modelled as
        a stack for DFS). This way, we guarantee we are always exploring
        the minimum cost path by popping the root of the min heap (greedy).

        This is the idea behind Dijkstra's Algorithm, which is used to find
        the min-path from one node to every other node in a graph.

    Runtime:
        Building the adjacency list still takes O(E).

        Using the min-heap, we relax every edge only once. When we relax
        it, we push onto the heap which costs O(log V). Since we have E
        edges, this leads to O(E * log V) time.

        Finding the highest delay takes O(V) time.

        Overall, we have O(E * log V) time.

    Memory:
        Adjacency list takes O(E) space.

        Priority queueu (min heap) can hold at most all nodes before we
        pop anything, so O(V).

        'times' array takes O(V) space.

        Overall, same O(V + E) space complexity as Solution1.
    """

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adj list with weights/delays
        adj = [[] for _ in range(n + 1)]
        for u, v, delay in times:
            adj[u].append((v, delay))

        # init
        pQ = []
        heapq.heappush(pQ, (0, k))
        # keep track of min time to reach each node from k
        times = [inf] * (n + 1)
        times[0] = 0  # index 0 is tombstone since nodes are 1-indexed
        times[k] = 0  # start node transmits to self in 0 time

        # traverse graph
        while pQ:
            time, node = heapq.heappop(pQ)

            # we found a better path already, so skip
            if time > times[node]:
                continue

            for nei, delay in adj[node]:
                newTime = time + delay

                # only keep exploring if it's worth it
                # i.e. current time with delay leads to a minimum
                if newTime < times[nei]:
                    times[nei] = newTime
                    heapq.heappush(pQ, (newTime, nei))

        # compute result
        res = max(times)
        return res if res != inf else -1
