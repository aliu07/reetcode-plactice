from typing import List


class Solution:
    """
    Intuition:
        We rely on calculating deltas to figure out how much time each car would
        take to reach the target given its initial position.

        We use a stack since the problem states that cars cannot pass each other.
        This points us to managing the stack in a specific way. We can think of
        fleets as a sequence of cars that are bottlenecked by the leading car (the
        one which they cannot overtake).

        This gives us an idea of how we should manage our stack. We can iterate
        over all the deltas. If we encounter a delta that is greater than the
        top-most delta on the stack, we know we currently have a 'bottleneck'
        car and must pop the previous delta (and repeat if the delta beneath the
        one we just popped is also smaller).

        At the end, we only have 'bottleneck'
        deltas remaining in our stack which equates to the number of fleets.

    Runtime:
        O(n) since we push/pop each element at most once onto/from the stack.

    Memory:
        O(n) for the stack and the deltas hashmap.

    """

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> List[int]:
        deltas = {p: (target - p) / s for p, s in zip(position, speed)}
        stack = []

        for p in sorted(position):
            while stack and stack[-1] <= deltas[p]:
                stack.pop()

            stack.append(deltas[p])

        return len(stack)
