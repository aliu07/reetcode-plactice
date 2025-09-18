# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
#
# DUMMY IMPLEMENTATION
def guess(num: int) -> int:
    return 0


class Solution:
    """
    Intuition:
        Use a binary search approach to find the target number.

    Runtime:
        O(log n)

    Memory:
        O(1)
    """

    def guessNumber(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            mid = (l + r) // 2

            # Our guess was too low
            if guess(mid) == 1:
                l = mid + 1
            # Our guess was too high
            elif guess(mid) == -1:
                r = mid
            else:
                return mid

        # Should never reach this point
        return -1
