class Solution:
    """
    Intuition:
        We can use 2 pointers to traverse each substring. However, we need to
        take into account odd and even palindromes. Thus, at each index, we
        need to check both cases.

    Runtime:
        O(n) -> consider the case where the substring is of the same length
        as the input string.

    Memory:
        O(1) -> we're only manipulating pointers.
    """

    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # Odd palindromes
            l, r = i, i

            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

            # Even palindromes
            l, r = i, i + 1

            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

        return res
