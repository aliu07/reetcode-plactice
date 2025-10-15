from typing import List
from collections import deque
import heapq


class Solution:
    """
    Intuition:
        Intuitively, we know that we have to start by processing
        the most frequent task. We resort to a maxHeap for efficient
        retrieval based on highest frequency.

        Then, we need a data structure to model the cooldown period.
        For this, we use a queue where each element contains the
        remaining frequency of the current task as well as the time
        value at which it can be scheduled again (after the cooldown).

    Runtime:
        Computing the frequency of the tasks takes O(n).

        For building the heap, we have a runtime of O(K log K) where
        K is the number of tasks. We know that there are at most 26
        unique tasks (number of letters in alphabet), so the runtime
        simplifies to O(1).

        The while loop either idles or decrements the frequency of a
        task. Given that we have n tasks, the runtime resolves to O(n)
        since each task needs to be treated.

        Overall, we have a runtime of O(n).

    Memory:
        O(1) for the heap and queue since there are at most 26 letters.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1

        maxHeap = []
        for k, v in freq.items():
            heapq.heappush(maxHeap, -v)

        # cooldown queue: store as (freq, cooldown end time)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                # +1 since we are dealing with negative values
                # equivalent of decrementing by 1...
                f = heapq.heappop(maxHeap) + 1

                if f < 0:
                    q.append((f, time + n))

            if q and q[0][1] == time:
                f, _ = q.popleft()
                heapq.heappush(maxHeap, f)

        return time
