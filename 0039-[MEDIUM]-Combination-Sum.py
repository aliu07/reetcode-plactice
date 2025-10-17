from typing import List


class Solution:
    """
    Intuition:
        We use a brute-force DFS approach to solve this problem. At each step, we
        try to add every number in nums to our current combination. If the sum of
        the current combination equals target, we add it to our result set. If the
        sum exceeds target, we backtrack.

    Runtime:
        Let n be the length of nums and t be the target value.

        In the worst case, we can have a combination of length t (if nums contains
        1). At each step, we have n choices (the numbers in nums). Therefore, the
        time complexity is O(n^t) since we have n branches at each recursive step
        and the depth is at most t.

    Memory:
        The call stack takes O(h) where h is the height of the recursion tree. We
        mentioneed this value to be t previously, so the overall memory complexity
        is O(t).
    """

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()

        # currently chosen, current sum, nums we can choose from
        def dfs(currNums, currSum):
            if currSum == target:
                currNums.sort()
                currNums = tuple(currNums)

                if currNums not in res:
                    res.add(currNums)

                return
            elif currSum > target:
                return

            # try with every single num
            for n in nums:
                copy = currNums.copy() + [n]
                dfs(copy, currSum + n)

        dfs([], 0)
        return [list(elmt) for elmt in res]
