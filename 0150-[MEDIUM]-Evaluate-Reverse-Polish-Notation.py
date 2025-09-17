from typing import List

class Solution:
    """
    Intuition:
        We store integer tokens on the stack. Whenever we hit an operand, we
        pop the numbers and perform the operation. Then, we push the result
        back onto the stack and continue processing until we are out of tokens.

    Runtime:
        Each token is processed once. The arithmetic operations and popping from
        the stack all take constant time. Thus, the overall time complexity is
        O(n).

    Memory:
        O(n) for the stack.
    """

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                n2, n1 = stack.pop(), stack.pop()
                res = 0

                match t:
                    case "+":
                       res = n1 + n2
                    case "-":
                        res = n1 - n2
                    case "*":
                        res = n1 * n2
                    case "/":
                        res = int(n1 / n2)

                stack.append(res)

        return stack[0]
