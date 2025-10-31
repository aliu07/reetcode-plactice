from typing import List


class Solution:
    """
    Intuition:
        The brute force approach would be to reduce this problem
        to Word Search I and iterate over each word. However,
        this is inefficient.

        We can use a trie to insert all of our words. This way,
        we can iterate through our matrix and search for many
        potential words at once.

        We use DFS to search at each cell, checking at each
        recursive step if we reached a valid word in the trie.

    Runtime:
        Inserting a word takes O(t) where t is the length
        of the word. Let k be the length of the longest
        word. It takes O(n * k) time to insert all words.

        Running a single invocation of DFS takes at most
        O(4 * 3^(t - 1)) time where t is the length of the
        word. This is because we have up to 4 choices of
        directions on the first iteration, and 3 on every
        subsequent recursive call (hence exponent of t - 1).

        We need to run DFS at each cell of which we have
        M * N (note N != n -> N = num of cols, n = num of
        words).

        Therefore, our total runtime is
        O(n * k) + O(M * N * 4 * 3^(t - 1)) which gives us
        an upper bound of O(M * N * 4 * 3^(t - 1)).

    Memory:
        O(26 * k * n) where n is the number of words and k is
        length of the longest word.

        The call stack also takes at most O(k).

        Overall O(n * k) space complexity.
    """

    class Trie:
        def __init__(self):
            self.root = {}

        def insert(self, word):
            curr = self.root

            for c in word:
                if c not in curr:
                    curr[c] = {}

                curr = curr[c]

            curr["#"] = True  # mark end of word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.Trie()
        for w in words:
            trie.insert(w)

        M, N = len(board), len(board[0])
        res = []

        def dfs(r, c, node, word):
            # out of bounds
            if r < 0 or r >= M or c < 0 or c >= N:
                return

            # if current char not in node's children
            if board[r][c] not in node:
                return

            # visited this cell alr
            if board[r][c] == ".":
                return

            # mark visited
            tmp = board[r][c]
            board[r][c] = "."

            # get next node
            node = node[tmp]
            word += tmp

            if node.get("#", False):
                res.append(word)
                # send end of word to false now to prevent duplicates
                node["#"] = False

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # remove tombstone
            board[r][c] = tmp

        res = []

        for r in range(M):
            for c in range(N):
                dfs(r, c, trie.root, "")

        return res
