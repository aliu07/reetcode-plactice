from typing import List

class Solution:
    """
    Intuition:
        Implementing a brute force solution that runs in O(n^2) is trivial. This solution
        would involve iterating over the rest of the array at each element to find a greater
        temperature.

        To avoid having to perform this repeated work, we can store previous temperatures
        somehow and come back to them whenever we encounter a larger temperature. A stack
        would be perfect for this!

        We push onto the stack whenever we encounter a temperature. Then, when we process
        the next, we peek onto the stack and pop so long as the previous temperature is
        smaller than the current one.

        Note that we do not need to store temperature values and can only store indices.

    Runtime:
        Each temp is processed once (and pushed/popped from the stack at most once). These
        operations all take constant time, so the overall runtime is O(n).

    Memory:
        O(n) for the stack.
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                res[j] = i - j

            stack.append(i)

        return res
