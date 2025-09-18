class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie1:
    """
    Intuition:
        The idea behind a Trie is to store a tree-like data structure where
        each level of the tree represents a character and its position in
        a string.

        For example, a TrieNode at the root level (i.e. level 0) means that
        we stored a word starting with that letter (i.e. position index 0)

        We also need to encode some additional metadata to mark if a node is
        the end of a word. This is needed since we have 2 types of lookups:
        word searches where we would check the end of word flag and prefixes
        where we don't care if the word ends or not so long as the sequence
        exists in the Trie.

    Runtime: O(n) for inserts and lookups

    Memory: O(n) where n is the total number of words

    Notes:
        Instead of creating a class to represent the TrieNodes, we can accelerate
        runtime by using a native dictionary. See Trie2.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            ix = ord(c) - ord("a")

            if not curr.children[ix]:
                curr.children[ix] = TrieNode()

            curr = curr.children[ix]

        # Mark end of word
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            ix = ord(c) - ord("a")

            if not curr.children[ix]:
                return False

            curr = curr.children[ix]

        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            ix = ord(c) - ord("a")

            if not curr.children[ix]:
                return False

            curr = curr.children[ix]

        return True


class Trie:
    """
    Intuition:
        Same as Trie1, except with dictionaries instead of custom class.
        We also use special character to encode the isEndOfWord boolean.
    """

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr:
                curr[c] = {}

            curr = curr[c]

        # Mark end of word
        # We use the '#' special character to encode the end of word bool
        curr["#"] = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr:
                return False

            curr = curr[c]

        return curr.get("#", False)

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr:
                return False

            curr = curr[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
