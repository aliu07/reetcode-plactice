from typing import List


class Solution:
    """
    Intuition:
        We use a DFS approach to model our binary decision tree. At each
        step, we can either decide to just add the next character or to
        look for a palindrome and add that to our partition.

        Our base case presents the termination condition required to end
        the search, at which point we append the found partition to our
        result.

        In our for-loop with jx, our upper bound is len(s) + 1 due to how
        string slices work in Python (excludes end index, so need one more
        position).

    Runtime:
        We have a binary decision at each recursive step with a maximum
        recursion depth of n. This leads to a O(2^n) runtime.

        It takes at most O(n) to check if a substring of the partition
        is a palindrome.

        Thus, we have an overall runtime of O(n * 2^n).

    Memory:
        We have 2^n ways of partitioning the input string.

        A partition will have at most n elements if you split string into
        individual characters.

        Therefore, our overall memory complexity is O(n * 2^n).
    """

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(ix, partition):
            if ix >= len(s):
                res.append(partition.copy())
                return

            # without palindrome - just pick next char
            partition.append(s[ix])
            dfs(ix + 1, partition)
            partition.pop()

            # with palindrome - check that its length is greater than 1
            for jx in range(ix + 2, len(s) + 1):
                substr = s[ix:jx]
                if substr == substr[::-1]:
                    partition.append(substr)
                    dfs(jx, partition)
                    partition.pop()

        dfs(0, [])
        return res


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(ix, partition):
            if ix >= len(s):
                res.append(partition.copy())
                return

            for jx in range(ix + 1, len(s) + 1):
                substr = s[ix:jx]
                if substr == substr[::-1]:
                    partition.append(substr)
                    dfs(jx, partition)
                    partition.pop()

        dfs(0, [])
        return res
