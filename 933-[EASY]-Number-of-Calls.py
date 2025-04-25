import heapq
from collections import deque

class RecentCounter1:
    """
    Intuition:
        We need to maintain a data structure to hold all the ping events.
        We also need an efficient way to filter out pings by time intervals.
        For this, we can use the idea of a min-heap. Whenever we receive a
        new ping, we pop from the heap as long as the oldest (i.e. smallest)
        ping is outside the defined interval of t - 3000.

    Notes:
        Using a heap causes inefficient insertion time, can definitely find
        a better data structure...

    Runtime:
        O(log n) for worst case insertion... need up to log n bubble up operations

        O(1) for while loop. We pop at most 3000 pings and O(3000) ~ O(1)

        Overall, O(log n)

    Memory: O(n) at worst holds all pings
    """

    def __init__(self):
        self.heap = []

    def ping(self, t: int) -> int:
        heapq.heappush(self.heap, t)

        while self.heap[0] < t - 3000:
            heapq.heappop(self.heap)

        return len(self.heap)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



class RecentCounter2:
    """
    Intuition:
        Since we know we receive pings in order, we can just use an
        array to model the queue of events. Thus, whenever we receive
        a new ping, we just append it and filter out the pings that
        fall outside the interval by popping from the left.

    Runtime:
        Insertion to the queue happens in O(1) now instead of O(log n)
        using a heap.

        Therefore, overall runtime is now bounded at O(1)... better!

    Memory: Still O(n)
    """

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
