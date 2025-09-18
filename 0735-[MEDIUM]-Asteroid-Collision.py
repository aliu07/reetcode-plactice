from typing import List


class Solution1:
    """
    Intuition:
        We use a stack to maintain state of asteroids. Notice that we only need
        to perform collision detection whenever we encounter an asteroid traveling
        towards the left.

    Notes:
        SO MANY SUBCASES... surely there's a better way of writing this...

    Runtime: O(n)
        Because every asteroid is only added to the stack once and potentially
        popped once despite the inner while loop seeming expensive.

    Memory: O(n)
    """

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # Either stack is empty or positive number
            if not stack or a > 0:
                stack.append(a)
            # Case negative number
            else:
                while True:
                    # If negative number cleared entire stack, it becomes
                    # new first element
                    if not stack:
                        stack.append(a)
                        break

                    peek = stack[-1]

                    # If previous asteroid also negative, then traveling
                    # in same direction... just append
                    if peek < 0:
                        stack.append(a)
                        break
                    # Case peeked asteroid is positive (i.e. calculate collision)
                    else:
                        # Case curr asteroid is smaller (it gets destroyed)
                        if abs(a) < peek:
                            break
                        # Case curr asteroid is larger in size
                        elif abs(a) > peek:
                            stack.pop()
                            break
                        # Case both asteroids are same size
                        else:
                            stack.pop()
                            break

        return stack


class Solution2:
    """
    Intuition:
        Same approach as solution 1 with a stack. Just cleaner way of writing
        it.

    Notes:
        YOU CAN USE AN ELSE BLOCK WITH WHILE LOOPS IN PYTHON?????
    """

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # While there are asteroids to collide and we have an asteroid
            # traveling left.
            while stack and a < 0 < stack[-1]:
                # Asteroid at the top of stack is smaller in size
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                # Asteroid at the top of stack is same
                elif stack[-1] == abs(a):
                    stack.pop()
                # Asteroid at the top of stack is larger
                break
            # Current asteroid is positive
            else:
                stack.append(a)

        return stack
