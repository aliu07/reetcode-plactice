class Solution:
    """
    Intuition:
        Use modulo and integer division to slowly consume
        input 'x' and build the reversed number.

    Runtime:
        O(log_10(x)). Note the log base of 10.

    Memory:
        O(1)
    """

    def reverse(self, x: int) -> int:
        LOWER, UPPER = -(2**31), 2**31 - 1
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            rev = (rev * 10) + (x % 10)
            x = x // 10

        res = sign * rev
        return res if LOWER <= res <= UPPER else 0
