from collections import Counter

class Solution1:
    """
    Intuition:
        We are given 2 possible operations:
            1) Swap any two existing characters in a word
            2) Transform every occurrence of one existing character into another existing
               character, and do the same with the other character.

        What does this mean for us? It means that 2 strings are close as long as every
        character in word1 also exists in word2 and the frequencies (occurrences of each
        character) match up.

    Runtime:
        O(n) since we need to build the hashsets and frequence counting arrays.

    Memory:
        O(n) to store the hashsets and arrays.

    Notes:
        The runtime of this solution is very slow on the LeetCode platform. We can rely on
        built-in data structures to accelerate our performance significantly.
    """

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        # Check available chars
        chars1 = set()
        chars2 = set()

        # Check frequency of chars
        freq1 = [0] * 26
        freq2 = [0] * 26

        for c1, c2 in zip(word1, word2):
            chars1.add(c1)
            chars2.add(c2)

            freq1[ord(c1) - ord('a')] += 1
            freq2[ord(c2) - ord('a')] += 1

        return sorted(freq1) == sorted(freq2) and chars1 == chars2



class Solution2:
    """
    Intuition:
        Same as Solution1.

    Runtime:
        O(n) as well.

    Memory:
        O(n) as well.
    """

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        map1 = Counter(word1)
        map2 = Counter(word2)

        # Sorting is not expensive here since collection has length of at most 26
        return map1.keys() == map2.keys() and sorted(map1.values()) == sorted(map2.values())
