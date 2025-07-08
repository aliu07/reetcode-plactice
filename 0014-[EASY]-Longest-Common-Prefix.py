from typing import List

class Solution:
    """
    Intuition:
        The brute force solution is trivial. We would just compare the shortest
        string against every other string until the longest prefix is found.

        Instead, we can use a more efficient data structure. For prefix matching,
        we have tries. We can use it to insert every string given to us and find
        the longest prefix by checking at each iteration the number of keys
        stored in the current level of the trie.

    Runtime:
        O(N * k) to insert all the strings where N is the number of strings and
        k is the length of the longest string.

        O(s) to find the longest prefix where s is the length of the shortest
        string in the array.

        Overall runtime bounded by insertion i.e. O(N * k).

    Memory:
        The trie holds every character given to us in the input string array.
        Thus, the memory complexity is O(N * k) where N is the number of strings
        and k is the length of the longest string.
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for s in strs:
            trie.insert(s)

        curr = trie.root
        prefix = ""

        while len(curr) == 1:
            key = list(curr.keys())[0]

            if key == "#":
                break

            prefix += key
            curr = curr[key]

        return prefix


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr:
                curr[c] = {}

            curr = curr[c]

        # Mark end of word
        curr['#'] = {}

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr:
                return False

            curr = curr[c]

        return '#' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr:
                return False

            curr = curr[c]

        return True
