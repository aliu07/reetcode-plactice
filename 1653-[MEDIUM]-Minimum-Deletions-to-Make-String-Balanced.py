from math import inf


class Solution:
    """
    Intuition:
        This type is a prefix DP type of problem. You can definitely optimize,
        but the solution below provides the general idea.

        We start by preprocessing our input. We compute the cost at each index
        to remove all succeeding A's and preceeding B's.

        Then, we go index by index and figure out the cost i.e. num of deletions
        and return the smallest one.

    Runtime:
        O(n), we have 3 linear passes.

    Memory:
        O(n), we maintain cost arrays for A's and B's.
    """

    def minimumDeletions(self, s: str) -> int:
        costRemoveA = []  # cost to remove all succeeding A's after each index ix
        cntA = 0
        for c in s[::-1]:
            costRemoveA.append(cntA)
            if c == "a":
                cntA += 1
        costRemoveA = costRemoveA[::-1]

        costRemoveB = []  # cost to remove all preceeding B's before each index ix
        cntB = 0
        for c in s:
            costRemoveB.append(cntB)
            if c == "b":
                cntB += 1

        res = inf  # compute cost at each index and store min
        for i in range(len(s)):
            res = min(res, costRemoveA[i] + costRemoveB[i])

        return res
