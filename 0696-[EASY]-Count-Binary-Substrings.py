from itertools import pairwise


class Solution1:
    """
    Intuition:
        Brute force approach. We expand outward every time we hit a
        segment where we have 2 different characters -> either "01"
        or "10". Expand until consecutive condition is violated on
        either side.

    Runtime:
        O(N) for the outer for loop.

        O(N) for the inner while loop.

        O(N^2) overall.

    Memory:
        O(1) since we only have ptrs.
    """

    def countBinarySubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s) - 1):
            c1, c2 = s[i], s[i + 1]
            if c1 != c2:
                res += 1
                l, r = i - 1, i + 2

                while l >= 0 and r < len(s):
                    if s[l] != c1 or s[r] != c2:
                        break
                    res += 1
                    l -= 1
                    r += 1

        return res


class Solution2:
    """
    Intuition:
        We can maintain the length of the previous consecutive
        sequence in a `compressed` array. Combined with a 2 ptr
        approach, we can ditch the inner loop.

    Runtime:
        O(N) as we reduced to a single linear pass.

    Memory:
        O(N) now since we need to maintain an array. In the worst
        case, we have an alternating binary string like "0101010".
    """

    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        compressed = [0]
        l, r = 0, 0

        while r < len(s):
            if s[l] == s[r]:
                # as long as our curr seq <= prev seq, we incr result
                if r - l + 1 <= compressed[-1]:
                    res += 1
                r += 1
            else:  # consecutive chain broken
                #  save len of prev consecutive seq
                compressed.append(r - l)  # no +1 since we exclude `r` ptr
                l = r

        return res


class Solution3:
    """
    Intuition:
        Realize that we only ever need to track the length of the
        current consecutive sequence and the length of the previous
        consecutive sequence. Whenever our current chain is broken,
        we can increment our result by min(prev, curr).

    Runtime:
       O(N).

    Memory:
        O(1).
    """

    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        # prev = len of prev consecutive seq
        # curr = len of curr consecutive seq
        prev, curr = 0, 1

        # numbers = [1, 2, 3, 4, 5]
        # pairs = itertools.pairwise(numbers)
        # for pair in pairs:
        #     print(pair)
        #
        # Output:
        # (1, 2)
        # (2, 3)
        # (3, 4)
        # (4, 5)
        for c1, c2 in pairwise(s):
            if c1 == c2:
                curr += 1
            else:
                res += min(prev, curr)
                prev = curr
                curr = 1

        # since we only incr result when chars flip (0 -> 1 or vice versa),
        # we need to incr at the end to collect any uncounted substrings
        return res + min(prev, curr)
