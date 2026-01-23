from typing import List


class Solution:
    """
    Intuition:
        Don't have to manipulate array in place. Just
        build a new array starting with least significant
        digit and reverse it to get most significant on
        the left.

    Runtime:
        O(n)

    Memory:
        O(n) -- although technically O(1) auxiliary space.

    """

    def plusOne(self, digits: List[int]) -> List[int]:
        res = []

        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            sum = digits[i] + carry
            rem = sum % 10
            carry = sum // 10

            res.append(rem)

        if carry:
            res.append(1)

        return res[::-1]
