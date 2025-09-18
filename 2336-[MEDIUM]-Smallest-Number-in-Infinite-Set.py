import heapq


class SmallestInfiniteSet1:
    """
    Intuition:
        We track all numbers within a min-heap to be able to pop the smallest
        element in constant time. We also use a hashset data structure to
        perform constant time lookups.

    Runtime:
        __init__ -> The constraints specify only 1000 elements, so technically
        constant time. However, if we changed to an arbitrary amount of elements,
        then this method would be O(N) where N is the number of elements. It is
        important to note that the sorted array nums is a valid min-heap by
        default, so we do not need any overhead to heapify.

        popSmallest -> O(log N). Popping from a heap in Python encompasses 2
        operations. Popping the smallest element which takes O(1) and then
        switching the last element in the array representing the heap, putting
        it at index 0, and sifting it down (heapify) which takes O(log N).
        Removing from the hashset takes constant time.

        addBack -> O(log N). Performing the lookup and inserting the element
        into the hashset both take O(1) time. Inserting the element into the
        heap takes O(log N) since we append it at the end of the array
        representing the heap and sift up.

    Memory:
        The SmallestInfiteSet data structure class will take up O(1) space
        since we only store 1000 elements in the heap and hashset. However,
        if we had to store an arbitrary amount of values, then it would be
        O(N).
    """

    def __init__(self):
        # Valid min-heap by default
        self.nums = [i for i in range(1, 1001)]
        # Store all nums in a hashset for quick lookups
        self.hashset = set(self.nums)

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.nums)
        self.hashset.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.hashset:
            self.hashset.add(num)
            heapq.heappush(self.nums, num)


class SmallestInfiniteSet2:
    """
    Intuition:
        We can reduce the runtime complexity of the constructor. We know
        that the smallest possible number at instantiation is 1, so we set
        the current value accordingly. We still use a hashset and a heap,
        but only for numbers who have been popped and added back. Our
        invariant becomes that the numbers in the hashset and heaps are
        guaranteed to be smaller than the self.current value (since they
        have been previously popped and self.current would have been
        incremented as a result).

    Runtime:
        __init__ -> O(1) now! Better than previous solution!
        popSmallest -> Still O(log N)
        addBack -> Also still O(log N)

    Memory:
        Still O(N)
    """

    def __init__(self):
        # Keep track of current min (starts at 1 by default)
        self.current = 1
        # Keep track of numbers that have been popped, but added back
        # using heap data struct
        self.minHeap = []
        # Also store them in hashset for quick lookups
        self.addedBack = set()

    def popSmallest(self) -> int:
        if self.minHeap:
            smallest = heapq.heappop(self.minHeap)
            self.addedBack.remove(smallest)
            return smallest

        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.addedBack:
            heapq.heappush(self.minHeap, num)
            self.addedBack.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
