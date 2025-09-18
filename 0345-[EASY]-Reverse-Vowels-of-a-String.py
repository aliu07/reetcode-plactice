class Solution1:
    """
    Intuition:
        We build a list of all the vowels present in the input string.
        Then, we iterate through the string and keep track of an index
        in the vowels list that goes backwards such that wehenver we
        hit a vowel in the input string, we can find the corresponding
        reversed vowel.

    Notes:
        This solution is "brute force" in a way. This is just what came
        to mind looking at the problem.

        There exists a more elegant solution that requires only a single
        pass on the input string s instead of 2.
    """

    def reverseVowels(self, s: str) -> str:
        # Get vowels
        vowels = [char for char in s if char.lower() in "aeiou"]

        jx = len(vowels) - 1
        res = list(s)

        for i, char in enumerate(res):
            if char.lower() in "aeiou":
                res[i] = vowels[jx]
                jx -= 1

        return "".join(res)


class Solution2:
    """
    Intuition:
        Much like how we would write the implementation of reversing
        a list, we can use a 2 ptr approach here. The only "trickier"
        part is defining our cases inside the while loop.

    Notes:
        Only requires one linear pass. More optimal
    """

    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        l, r = 0, len(s) - 1
        res = list(s)

        while l <= r:
            if res[l] not in vowels:
                l += 1
            elif res[r] not in vowels:
                r -= 1
            else:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1

        return "".join(res)
