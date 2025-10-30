from collections import deque


class WordDictionary:
    """
    Intuition:
        We can use a try to insert words and then efficiently search them.

        Inserting words into the trie is straightforward.

        Searching is a harder since we need to deal with wildcards. Whenever
        we encounter one, we search through all the children of the current
        node. Note that the termination condition needs to continue exploring
        other potential paths and not return immediately.

    Runtime:
        O(n) to insert a word where n is the length of the word.

        O(n) to search a word where n is the length of the word.

    Memory:
        Let k be the length of the longest word we have.

        Then our Trie data structure will take up at most O(26 * k) ~ O(k)
        memory.
    """

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node:
                node[c] = {}

            node = node[c]

        # mark end of word
        node["#"] = True

    def search(self, word: str) -> bool:
        # (node, ix)
        q = deque([(self.root, 0)])

        while q:
            node, ix = q.pop()

            if ix == len(word):
                if node.get("#", False):
                    return True

                continue  # keep exploring other paths

            c = word[ix]
            if c == ".":
                for nei in node:
                    if nei != "#":
                        q.append((node[nei], ix + 1))
            elif c in node:
                q.append((node[c], ix + 1))

        return False
