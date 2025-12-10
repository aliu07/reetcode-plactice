from collections import defaultdict
from typing import List


class Solution:
    """
    Intuition:
        We want to build a Eulerian Path given a graph. We can Model
        the plane tickets as edges and the airports as vertices.

        We use Hierholzer's Algorithm to solve this problem. In
        essence, we maintain a stack of nodes. At each iteration,
        we peek the stack and check if the peeked node has an
        unexplored incident edge. If so, we keep going. If not, we
        add the current node to our result path.

    Runtime:
        Let V be the number of airports and E the number of tickets.

        Building the adj list takes O(E log E) time since we need to
        sort it.

        Each edge is processed once, leading to O(E) time to build
        the itinerary.

        Overall, we have O(E log E) runtime.

    Memory:
        Let V be the number of airports and E the number of tickets.

        The adjacency list takes O(E) space.

        The stack contains at most O(V) airports.

        Overall, we have O(V + E) memory complexity.

    """

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # build adj list
        adj = defaultdict(list)
        # reverse sorted list since we pop from end later on
        # we want to pop lexicographically smallest first
        for src, dest in sorted(tickets)[::-1]:
            adj[src].append(dest)

        stack = ["JFK"]
        res = []
        while stack:
            node = stack[-1]

            if adj[node]:
                stack.append(adj[node].pop())
            else:
                res.append(stack.pop())

        return res[::-1]
