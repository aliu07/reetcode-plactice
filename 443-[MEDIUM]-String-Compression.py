from typing import List

class Solution1:
    """
    Intuition:
        Use 2 pointers to keep track of each window of consecutive characters.
        Then, build result string representing compressed version and modify
        input array.

    Notes:
        This solution does not use constant auxiliary memory since the 'res'
        string grows linearly with the chars input array.
    """

    def compress(self, chars: List[str]) -> int:
        l = 0
        res = ""

        while l < len(chars):
            r = l

            while r < len(chars) and chars[l] == chars[r]:
                r += 1

            res += chars[l]

            if r - l > 1:
                res += str(r - l)

            l = r

        for i in range(len(res)):
            chars[i] = res[i]

        return len(res)



class Solution2:
    """
    Intuition:
        We can use the same 2 pointer approach, except this time we
        maintin constant memory by storing and tracking an insertion
        index.

        Whenever we finish calculating the left and right boundaries
        of our current sequence of consecutive chars, we know that
        the left pointer stores the character we are processing currently.
        The right pointer stores the character that comes after the last
        occurrence of the current sequence.

        Therefore, we can update the insertion index to the char at the
        left boundary.

        Then, we check the count of that character by evaluating the size
        of the window. If the length is greater than 1, then we need to
        process the length as well in our compressed format.

        Finally, we know that the final position of ix represents the end
        of our compressed string, so we return it.
    """

    def compress(self, chars: List[str]) -> int:
        l = 0
        ix = 0 # Insertion index

        while l < len(chars):
            r = l

            while r < len(chars) and chars[l] == chars[r]:
                r += 1

            chars[ix] = chars[l]
            ix += 1

            if r - l > 1:
                for char in str(r - l):
                    chars[ix] = char
                    ix += 1

            l = r

        return ix
