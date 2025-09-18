class Solution1:
    """
    Intuition:
        We can balance parentheses using a stack. The interesting part of
        this problem is that we need to remove invalid parentheses. Therefore,
        we need 1 pass to remove invalid ')' chars and then another pass to
        remove invalid '(' brackets.

        We keep track of invalid indices throughout each pass and return the result
        string without those invalid indices.

    Notes:
        This first solution's relative runtime is not super optimized since it
        does not leverage built-in functions in Python. The idea behind the
        logic is correct, though.

    Runtime: O(n)

    Memory: O(n)
    """

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid = set()  # Track invalid indices

        for i, char in enumerate(s):
            if char == "(":
                stack.append((char, i))

            if char == ")":
                if not stack:
                    invalid.add(i)
                else:
                    stack.pop()

        for char, i in stack:
            invalid.add(i)

        res = ""
        for i in range(len(s)):
            if i in invalid:
                continue

            res += s[i]

        return res


class Solution2:
    """
    Notes:
        Slightly optimized runtime.
    """

    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        numL = 0

        for char in s:
            if char == "(":
                numL += 1

            if char == ")":
                if numL == 0:
                    continue

                numL -= 1

            res.append(char)

        if numL == 0:
            return "".join(res)

        numR = 0
        for i in range(len(res) - 1, -1, -1):
            if res[i] == ")":
                numR += 1

            if res[i] == "(":
                if numR == 0:
                    res[i] = ""
                else:
                    numR -= 1

        return "".join(res)
