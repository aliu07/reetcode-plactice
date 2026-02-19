class Solution:
    """
    Intuition:
        Brute force approach. We expand outward every time we hit a
        segment where we have 2 different characters -> either "01"
        or "10". Expand until consecutive condition is violated on
        either side.

    Runtime:
        O(N) for the outer for loop.

        O(N) for the inner while loop.

        O(N^2) overall.

    Memory:
        O(1) since we only have ptrs.
    """

    def countBinarySubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s) - 1):
            c1, c2 = s[i], s[i + 1]
            if c1 != c2:
                res += 1
                l, r = i - 1, i + 2

                while l >= 0 and r < len(s):
                    if s[l] != c1 or s[r] != c2:
                        break
                    res += 1
                    l -= 1
                    r += 1

        return res
