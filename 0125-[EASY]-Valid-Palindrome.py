class Solution1:
    """
    Intuition:
        Use 2 pointer approach to iterate through string.
        Have logic to skip whitespace & non-alphanum chars.

    Notes:
        - Don't forget to cast chars to lowercase.
        - Can improve runtime using built-in funcs.
    """

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            while l < len(s) and not s[l].isalnum():
                l += 1

            while r >= 0 and not s[r].isalnum():
                r -= 1

            if l >= len(s) or r < 0:
                break

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True



class Solution2:
    """
    Improvements:
        - Use built-in functions
    """

    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s.lower() if char.isalnum())
        return s == s[::-1]
