from collections import deque
from typing import List


class Solution1:
    """
    Intuition:
        Recursive DFS. At each step, we can choose out of all the characters
        the phone digit can map to.

        Our base case (termination condition) is when the letter string reaches
        the length of our input digit string.

    Runtime:
        We have between 3 and 4 characters per digit. Assuming n digits, this
        gives us a runtime of O(4^n) in the worst case.

        Constructing the string from "".join(curr) takes O(n) time.

        Overall, we have a O(n * 4^n) runtime.

    Memory:
        The curr array takes at most O(n) space.

        We have 4^n possibilities, leading to O(n * 4^n) for the result array.

        Thus, we have O(n) auxiliary space or O(n * 4^n) space in total.
    """

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def dfs(ix, curr):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return

            nextDigit = digits[ix]
            for c in digitMap[nextDigit]:
                curr.append(c)
                dfs(ix + 1, curr)
                curr.pop()

        dfs(0, [])
        return res


class Solution2:
    """
    Intuition:
        Same as Solution1. Iterative instead of recursive.

    Runtime:
        Same as Solution1.

    Memory:
        Same as Solution1.
    """

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        q = deque([(0, "")])

        while q:
            ix, curr = q.pop()

            if len(curr) == len(digits):
                res.append(curr)
                continue

            for c in digitMap[digits[ix]]:
                q.append((ix + 1, curr + c))

        return res
