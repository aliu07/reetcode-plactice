class Solution1:
    """
    Intuition:
        Similar to merge 2 sorted linked lists problem. Use 2 pointers
        and iterate through both strings while building result. At the
        end, if a string is longer, just append the rest.

    Runtime: O(n)

    Memory: O(n)
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        ix1, ix2 = 0, 0

        while ix1 < len(word1) and ix2 < len(word2):
            res += word1[ix1]
            res += word2[ix2]
            ix1 += 1
            ix2 += 1

        if ix1 < len(word1):
            res += word1[ix1:]

        if ix2 < len(word2):
            res += word2[ix2:]

        return res



class Solution2:
    """
    Intuition:
        Same approach as solution 1. Just wanted to write a working solution
        using zip() in Python.

    Notes:
        Runtime is on same scale, but a lot slower... probably due to overhead
        of zipping.
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        res = ""

        for c1, c2 in zip(word1, word2):
            res += c1
            res += c2

        if m > n:
            res += word1[n:]
        elif n > m:
            res += word2[m:]

        return res
