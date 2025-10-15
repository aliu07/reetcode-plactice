import heapq


class MedianFinder:
    """
    Intuition:
        We can partition the stream into 2 heaps like so:
        - minHeap represents the upper range of numbers with the
          smallest number at the root for quick access
        - maxHeap represents the lower range of numbers with the
          greatest number at the root for quick access

        By splitting the data stream like so, we can compute the
        median efficiently since we can access our middle values
        in constant time from the heaps.

    Runtime:
        O(log n) for a single call to addNum.

        O(1) for a single call to findMedian.

        If we have m function calls to each, then O(m log n) for
        addNum and O(m) for findMedian.

    Memory:
        Both heaps contain the total number of numbers in the stream.
        Thus, the overall memory complexity is O(n).
    """

    def __init__(self):
        # right partition of stream (nums greater than median)
        self.minHeap = []
        # left partition of stream (nums smaller than median)
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        # push num based on roots of heaps
        if self.maxHeap and -num > self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # rebalance heaps
        if len(self.maxHeap) > len(self.minHeap) + 1:
            popped = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, popped)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            popped = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -popped)

    def findMedian(self) -> float:
        # case even num of elmts in stream
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        # cases odd num of elmts in stream
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]
