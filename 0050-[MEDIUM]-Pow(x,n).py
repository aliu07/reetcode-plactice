class Solution1:
    """
    Intuition:
        Brute force approach to compute the power.

    Notes:
        - Exceeds runtime limits.
        - Need a better way...
    """

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        res = 1

        for i in range(abs(n)):
            res *= x

        return res if n > 0 else 1 / res



class Solution2:
    """
    Intuition:
        Use a divide and conquer approach to solve problem
        in log time. Define base case when exponent is 0.
        Then, we have 2 recursive cases where either the
        exponent is odd or even.

    Notes:
        - Can be improved by writing iterative solution
    """

    def myPow(self, x: float, n: int) -> float:
        def helper_pow(x, n):
            if n == 0:
                return 1

            half = helper_pow(x, n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        res = helper_pow(x, abs(n))
        return res if n > 0 else 1 / res



class Solution3:
    """
    Intuition:
        Improve runtime using iteration rather than recursion.
        We square the base 'x' at every iteration. If the remainder
        of the current power modulo 2 is 1, then we multiply the
        result by the current base 'x'. This works due to the binary
        representation of the power 'n'.

    Example:
        - n = 13, binary = 1101
        - Then x^13 = x^8 * x^4 * x^1
        - Check the binary of the exponent and whenever the bit is 1,
          multiply result by value in that bit's position.
    """

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        power = abs(n)
        res = 1.0

        while power > 0:
            if power % 2 == 1:
                res *= x

            x *= x
            power = power // 2

        return res if n > 0 else 1 / res
