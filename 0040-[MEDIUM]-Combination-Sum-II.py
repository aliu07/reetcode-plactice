from typing import List


class Solution1:
    """
    Intuition:
        We use DFS backtracking to sovle this problem. Unlike the previous
        Combination Sum problem, each number can only  be used once. Thus,
        we need some extra logic to handle duplicates.

        Our base cases are as follows:
        - If our current combination reaches the target, we make a copy and
          append it.
        - If our current sum exceeds the target, then we return early.
        - If the index goes out of range, then we also return early.

        At each step, we have 2 choices:
        1. Include the current number in our combination.
        2. Skip the current number and all subsequent duplicates.

    Runtime:
        We have a binary recursion tree -> 2 decisions at each recursive step
        i.e. picking or skipping. This means a O(2^n) runtime in the worst
        case.

        Each combination needs to be copied. A combination has at most n elmts.

        Thus, the overall runtime is O(n * 2^n).

    Memory:
        Call stack depth is at most O(n).
    """

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(ix, currComb, currSum):
            # found a combination
            if currSum == target:
                res.append(currComb.copy())
                return

            # exceed target or run out of candidates
            if currSum > target or ix == len(candidates):
                return

            # include candidates[ix]
            currComb.append(candidates[ix])
            dfs(ix + 1, currComb, currSum + candidates[ix])
            currComb.pop()
            # skip curr position and subsequent duplicates
            while ix + 1 < len(candidates) and candidates[ix] == candidates[ix + 1]:
                ix += 1
            dfs(ix + 1, currComb, currSum)

        dfs(0, [], 0)
        return res


class Solution2:
    """
    Intuition:
        Same overall intuition as Solution1. We simplify the logic for skippig
        duplicates and breaking early upon encountering an element that makes
        our combintion exceed the target by handling it in the for loop.

    Runtime:
        Still a binary decision tree, so O(2^n).

        Copying combinations takes at most O(n) time.

        Overall still O(n * 2^n) time.

    Memory:
        Call stack depth is at most O(n).

        Combination storage also at most O(n).

        Overall O(n) space.
    """

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(ix, currComb, currSum):
            # found a combination
            if currSum == target:
                res.append(currComb.copy())
                return

            for j in range(ix, len(candidates)):
                # skip duplicates
                if j > ix and candidates[j] == candidates[j - 1]:
                    continue

                # exceeds target, we can exit at this point
                if currSum + candidates[j] > target:
                    break

                currComb.append(candidates[j])  # pick curr elmt
                dfs(j + 1, currComb, currSum + candidates[j])  # continue exploring at next elmt
                currComb.pop()  # backtrack

        dfs(0, [], 0)
        return res
