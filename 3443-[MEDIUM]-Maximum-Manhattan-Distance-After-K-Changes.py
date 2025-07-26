class Solution:
    """
    Intuition:
        Calculating the Manhattan of the input string is trivial. The
        insight is that we should switch the least frequent letters
        in the vertical and horizontal directions to maximize our distance.

        Note that for every letter flipped, we can increase the distance
        by 2. Therefore, with up to k flips, we can increase the Manhattan
        distance by at most k * 2.

        However, also note that the maximum Manhattan distance possible
        is equal to the length of the input string. This is sets a hard
        upper bound to our maximum possible distance.

        Thus, we check at each iteration the number of occurrences of each
        direction, and compute the potential maximum Manhattan distance
        by taking the current x and y and adding k * 2. We use the min()
        function to make sure that we don't exceed the maximum upper bound.

    Runtime:
        O(N) since we need 1 pass to traverse the string.

    Memory:
        O(1) obviously.
    """
    def maxDistance(self, s: str, k: int) -> int:
        x, y = 0, 0
        res = 0

        for ix, c in enumerate(s):
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            elif c == 'W':
                x -= 1

            res = max(res, min(abs(x) + abs(y) + 2 * k, ix + 1))

        return res
