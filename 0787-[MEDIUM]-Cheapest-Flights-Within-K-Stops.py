from math import inf


class Solution:
    """
    Intuition:
        Using Bellman-Ford algorithm. At each iteration of the
        for loop, we are propagating min costs across an extra
        stop from each node. At the end, we can just peek the
        price at the index of our destination airport.

    Runtime:
        Suppose we have n flights available.

        The outer for loop takes k iterations. For each of those
        k iterations, we need to create a new array to hold the
        updated prices and iterate through all flights which both
        take O(N) time.

        Thus, the total runtime is O(k * n).

    Memory:
        The prices array takes O(n) space.

        Every tmp array we allocate also takes O(n) space.

        Overall, O(n) memory complexity.
    """

    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [inf] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices[:]
            for u, v, cost in flights:
                if prices[u] + cost < tmp[v]:
                    tmp[v] = prices[u] + cost
            prices = tmp  # update layer

        return prices[dst] if prices[dst] < inf else -1
