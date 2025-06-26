from typing import List

class Solution:
    """
    Intuition:
        The key observation is to keep track of the amount of open brackets.
        At each step, if we still have capacity for open brackets, we will
        always compute the subcase of adding an extra open bracket. For closing
        brackets, the logic is a bit more complex. We need to ensure that we
        the number of open brackets in the current string is greater than the
        number of closed brackets. To do this, we can simply evaluate by checking
        the length of the string and the number of open brackets stored in the
        'open' variable.

    Runtime:
        Although the runtime looks exponential, it is bounded by Catalan numbers.
        What are Catalan numbers? I have no idea, but chat gippity says they're
        some type of combinatorial relationship. The overall runtime would be
        O( 4^n / [n^(3/2) * pi^(1/2)]) ~ O(4^n / n^(3/2)).

    Memory:
        Same complexity as runtime i.e. O(4^n / n^(3/2)).
    """

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, curr):
            if len(curr) == 2 * n:
                res.append(curr)

            if open < n:
                dfs(open + 1, curr + '(')

            if open > len(curr) / 2:
                dfs(open, curr + ')')

        dfs(0, '')

        return res
