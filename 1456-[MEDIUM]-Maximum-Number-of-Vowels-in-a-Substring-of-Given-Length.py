class Solution:
    """
    Intuition:
        This problem fits the requirements of a fixed sliding window problem.
        We use k as the size of our window and slide it along the string to
        verify all substrings.

    Notes:
        This solution isn't super elegantly written. Later solutions will
        improve on this. It's a good starting point though.

    Runtime: O(n)

    Memory: O(1)
    """

    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        l, r = 0, 0
        curr, res = 0, 0

        while r < len(s):
            # Reached max window size
            if r - l + 1 > k:
                if s[l] in vowels:
                    curr -= 1
                    res = max(res, curr)

                l += 1
            # Can still increment window
            else:
                if s[r] in vowels:
                    curr += 1
                    res = max(res, curr)

                r += 1

        return res
