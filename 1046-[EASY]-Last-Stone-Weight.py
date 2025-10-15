import heapq
from typing import List


class Solution:
    """
    Intuition:
        Model stones as a max heap. Then, iterate over the
        heap until there is either a single stone left or
        none left.

    Runtime:
        Building the heap and heapify each take O(n) time.

        Each pop/push operation takes O(log n) time. Each
        iteration of the loop reduces the size of the heap
        by at least one. Thus, we have O(n) in the worst
        case where the loop runs until there is at most
        one stone left.

    Memory:
        stones array used as heap data structure, so O(n)
        space.
    """

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # x = heaviest, y = 2nd heaviest
            x, y = heapq.heappop(stones), heapq.heappop(stones)

            # we have x < y since elmts are negative, so
            # x < y means in reality that x heavier than y
            if x < y:
                heapq.heappush(stones, x - y)

        return abs(stones[0]) if stones else 0
