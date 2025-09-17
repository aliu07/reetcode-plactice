class Solution:
    """
    Intuition:
        We maintain a map of bracket pairings and a stack. Whenever we encounter a closing
        bracket/parenthesis, we check the top of the stack. At the end, we check if there
        is anything left in the stack to ensure that all brackets have been paired.

    Runtime:
        Each character in the input string is processed once, so the time complexity is O(n).

    Memory:
        The stack contains at most half the characters in s which gives us O(n / 2). However,
        this still simplifies to O(n).
    """

    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []

        for c in s:
            if c not in pairs:
                stack.append(c)
            elif not stack or stack[-1] != pairs[c]:
                return False
            else:
                stack.pop()

        return len(stack) == 0
