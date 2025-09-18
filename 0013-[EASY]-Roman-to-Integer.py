class Solution:
    """
    Intuition:
        Store a map for constant time lookups. We traverse the
        input roman number with an index pointer and check for
        special cases such as 'IV', 'XL', 'LC', etc.

    Runtime:
        O(n) since we need to traverse the entire input string.

    Memory:
        O(1) since the map is bounded.
    """

    def romanToInt(self, s: str) -> int:
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0
        ix = 0

        while ix < len(s):
            # Special case: encounter 4, 40, 400, etc.
            if ix < len(s) - 1 and map[s[ix]] < map[s[ix + 1]]:
                res += map[s[ix + 1]] - map[s[ix]]
                ix += 2
            # Regular case
            else:
                res += map[s[ix]]
                ix += 1

        return res
