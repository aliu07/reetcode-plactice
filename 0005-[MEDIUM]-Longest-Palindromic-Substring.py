class Solution1:
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
        N = len(s)
        res = ""
        resLen = 0

        for i in range(N):
            # Odd palindromes
            l, r = i, i

            while 0 <= l and r < N and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

            # Even palindromes
            l, r = i, i + 1

            while 0 <= l and r < N and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

        return res


class Solution2:
    """
    Intuition:
        We can use a look-up matrix to track if a substring starting
        at i and ending at j is palindromic.

        We start by initializing our base cases or palindromic "cores"
        which include all single character substrings and repeating char
        substrings.
    """

    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        # dp[i][j] = true if the substring s[i..j] (inclusive) is a palindrome
        #          = false otherwise
        dp = [[False] * N for _ in range(N)]
        res = ""

        # init base cases
        for i in range(N):
            # odd palindromes
            dp[i][i] = True

            if not res:
                res = s[i]

            # even palindromes
            if i < N - 1:
                is_palindrome = s[i] == s[i + 1]

                if is_palindrome:
                    dp[i][i + 1] = True
                    if len(res) < 2:
                        res = s[i : i + 2]

        for length in range(2, N + 1):
            for ix in range(N - length + 1):
                jx = ix + length - 1
                # need matching chars AND rest of inner substring is palindromic
                is_palindrome = (s[ix] == s[jx]) and dp[ix + 1][jx - 1]

                if is_palindrome:
                    dp[ix][jx] = True
                    if jx - ix + 1 > len(res):
                        res = s[ix : jx + 1]

        return res
