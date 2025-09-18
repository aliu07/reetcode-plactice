class Solution1:
    """
    Intuition:
        Use a 2 pointer approach to solve this problem. We can skip a singular
        invalid character, except this invalid character could be either on the
        left or right side. Thus, when we do encounter an invalid char, we need
        to check both cases.

    Notes:
        This is a vanilla approach with the right intuition. We can definitely
        use built-in Python methods and shorthands to speed up runtime.
    """

    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r, s):
            while l <= r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return is_palindrome(l, r - 1, s) or is_palindrome(l + 1, r, s)

            l += 1
            r -= 1

        return True


class Solution2:
    """
    Notes:
        Improved runtime by accelerating comparison with [::-1]

        skipL:
            skip the left invalid char
            so increment left boundary by 1
            we also need r + 1 to still include the right boundary

        skipR:
            skip the right invalid char
            so the interval is [l:r] since r is excluded here
    """

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1 : r + 1], s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]

            l += 1
            r -= 1

        return True
