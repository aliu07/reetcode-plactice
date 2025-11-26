from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Intuition:
        The biggest insight to solve this problem is to deal with generic patterns.

        The "brute force" way would be to build an adjacency list where each word
        maps to a list of words that differ by one letter. However, this would be
        very inefficient and most certainly exceed time limit.

        To build the adjacency list more efficiently, we can use wild cards, '*',
        to represent any character. Our keys in the map become patterns containing
        wild cards rather than actual words.

        After that, the problem is reduced to a BFS problem where we return the
        shortest path between the beginWord and endWords if it exists. Another thing
        to note here is the `seen` set. Instead of storing individual words, we
        store the seen patterns encountered so far. By storing patterns rather than
        words, we save ourselves the work of iterating over all the possible words
        of a pattern.

    Runtime:
        Let n be the number of words in wordList and k be the length of the longest
        word.

        To build the adjacency list, we iterate over all words in the list. This
        takes O(n) time. Then, we iterate over each index of the word which takes
        O(k) time. Finally, we build a pattern by using string slicing to insert
        a wildcard '*', which takes O(k) time too.

        Thus, the loop to build the adjacency list takes O(n * k^2) time.

        For the BFS loop, we process each word once which equates to O(n) time.
        For each word we process, we iterate over each index and generate the
        corresponding pattern which takes O(k^2) as previously mentionned.

        Thus, the BFS loop also takes O(n * k^2) time.

        Overall, our runtime is O(n * k^2).

    Memory:
        We can generate at most O(n * k) patterns. The longest pattern is O(k)
        long. Thus, the size of the adjacency list is O(n * k^2).

        The BFS queue contains at most all the words which is O(n * k) where
        O(n) is the number of words and O(k) the length of the longest word.

        The seen set contains at most all patterns which is O(n * k^2) where
        O(n * k) is the number of possible patterns and O(k) is the maximal
        length of a pattern.

        Thus, the overall memory complexity is O(n * k^2).
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # base case
        if endWord not in wordList:
            return 0

        # build adj list
        adj = defaultdict(list)
        for w in wordList:
            for ix in range(len(w)):
                pattern = w[:ix] + "*" + w[ix + 1 :]
                adj[pattern].append(w)

        # bfs to find min path
        res = 1
        q = deque([beginWord])
        seen = set()
        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for ix in range(len(word)):
                    pattern = word[:ix] + "*" + word[ix + 1 :]

                    if pattern not in seen:
                        seen.add(pattern)

                        for nei in adj[pattern]:
                            q.append(nei)

            res += 1

        return 0
