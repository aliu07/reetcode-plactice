class Solution:
    """
    Intuition:
        Maintain a stack of characters. Everytime we encounter a
        * character, we pop the last element on the stack.

    Notes:
        The constraint specifies that the operation described when
        we encounter a * character is GUARANTEED to be possible.

        Thus, we do not need to worry about edge cases (e.g. input
        string starting with *).
    """

    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
