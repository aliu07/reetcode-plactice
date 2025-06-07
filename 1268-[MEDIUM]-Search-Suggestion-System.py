from typing import List

class Solution:
    """
    Intuition:
        We can insert all the products into a Trie. At each iteration, we add a letter from the searchWord
        input variable which is essentially the prefix we are matching on. Then, we use DFS to find up to
        3 suggestions that contain the prefix.

    Runtime:
        O(M) to build the Trie where M is the total number of chars in products.

        For each prefix, we find its representative node in O(len(prefix)) time. Then, we use DFS to find at
        most 3 words which takes O(1) time.

        Thus, the overall complexity is dominated by the time required to build the Trie i.e. O(M).

    Memory:
        O(26 * n) ~ O(n) where n is the number of nodes in the Trie and 26 is the number of letters. The
        overall complexity can be simplified (we can remove the factor of 26 in big-O notation).

    Notes:
        Runtime performance is abysmal on LeetCode for this approach :(

        There exists a binary search approach that is much more efficient on the platform
    """

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Build Trie
        trie = self.Trie()

        for p in products:
            trie.insert(p)

        prefix = ""
        res = []

        for c in searchWord:
            prefix += c
            res.append(trie.getWordsStartingWith(prefix))

        return res

    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isEndOfWord = False

    class Trie:
        def __init__(self):
            self.root = Solution.TrieNode()

        def insert(self, word: str) -> None:
            curr = self.root

            for c in word:
                ix = ord(c) - ord('a')

                if not curr.children[ix]:
                    curr.children[ix] = Solution.TrieNode()

                curr = curr.children[ix]

            # Mark end of word
            curr.isEndOfWord = True

        def getWordsStartingWith(self, prefix: str) -> List[str]:
            curr = self.root
            words = []

            for c in prefix:
                ix = ord(c) - ord('a')

                if not curr.children[ix]:
                    return words

                curr = curr.children[ix]

            self.dfsWithPrefix(curr, prefix, words)

            return words

        def dfsWithPrefix(self, curr: 'Solution.TrieNode', word: str, words: List[str]):
            if len(words) == 3:
                return

            if curr.isEndOfWord:
                words.append(word)

            for i in range(26):
                if curr.children[i]:
                    self.dfsWithPrefix(curr.children[i], word + chr(i + ord('a')), words)
