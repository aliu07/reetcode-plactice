from collections import deque
from typing import List


class Solution:
    """
    Intuition:
        We parse all pairs of words to find the first difference. This
        difference yields us an edge in our graph. If we encounter a
        word that is longer coming after a shorter word and the shorter
        word is a prefix to the longer word, then there is no possible
        ordering.

        Then, we perform a topological sort on our graph using Kahn's
        algorithm. If the final ordering does not contain all letters,
        then it is invalid.

    Runtime:
        Let n be the num of words and k be the len of the longest word.

        To build the adj list, we iterate through all the words which
        takes O(n). For each pairing, we iterate through all the chars
        of each word which takes up to O(k). Combined, this yields
        O(n * k).

        Topological sort starts by scanning all nodes of which takes at
        most O(26) considering there are only 26 latin letters. Then,
        we process each edge at most once which gives O(E). The total
        runtime incurred here is O(E).

        Thus, overall runtime is O((n * k) + E).

    Memory:
        The adj list takes up to O(E) space.

        The in-degree dict tracks at most 26 chars, so O(1) space.

        The queue contains at most all nodes or chars which is O(26)
        or O(1) in simplified form.

        Thus, the overall memory complexity is O(E).

    """

    def alienOrder(self, words: List[str]) -> str:
        adj = {}
        in_degree = {}

        for w in words:
            for i in range(len(w)):
                adj[w[i]] = []
                in_degree[w[i]] = 0

        for i in range(1, len(words)):
            a, b = words[i - 1], words[i]

            # if a is longer, then it cannot possibly be
            # lexicographically smaller...
            if len(a) > len(b) and a[: len(b)] == b:
                return ""

            for ca, cb in zip(a, b):
                if ca != cb:
                    # only increment in-degree if edge did not exist
                    if cb not in adj[ca]:
                        in_degree[cb] += 1

                    adj[ca].append(cb)
                    # after finding 1st lexicographical difference, exit
                    break

        q = deque()
        for node in adj:
            if in_degree[node] == 0:
                q.append(node)

        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        # if topo ordering does not contain all nodes at this stage, it is invalid
        return "".join(topo) if len(topo) == len(adj) else ""
