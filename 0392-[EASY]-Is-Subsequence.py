class Solution:
    """
    Intuition:
        Use pointers to traverse each string. Only increment the
        pointer tracking the subsequence string 's' if the characters
        at p1 and p2 are equal. At the end, we check if p1 has reached
        the end of the string 's'.
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0

        while p2 < len(t):
            if p1 < len(s) and s[p1] == t[p2]:
                p1 += 1

            p2 += 1

        return p1 == len(s)
