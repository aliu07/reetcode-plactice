from typing import List


class Solution1:
    """
    Intuition:
        Brute force approach would maintain a set of subsets. We
        would then create all possible subsets and insert them into
        the set. However, this implementation is trivial and in-
        efficient.

        We will use a DFS backtracking approach.

        Our base case is when we reach the length of nums upon
        which we return.

        We then add the elmt at the current index and keep exploring.

        To avoid duplicate subsets, we skip all duplicates before
        selected a new elmt as the first elmt of our new subset.
        After that, we just keep exploring.

    Runtime:
        It takes at most O(n) to copy a subset.

        We have a binary recursive decision tree, so O(2^n).

        Overall, we have a runtime complexity of O(n * 2^n).

    Memory:
        Subset takes at most O(n) memory.

        O(2^n) for the result array.

        Overall, O(n) auxiliary space.
    """

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(ix, curr):
            if ix == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[ix])  # select curr
            dfs(ix + 1, curr)  # explore
            curr.pop()  # backtrack

            # skip duplicates
            while ix + 1 < len(nums) and nums[ix] == nums[ix + 1]:
                ix += 1
            dfs(ix + 1, curr)  # keep exploring

        nums.sort()
        dfs(0, [])
        return res


class Solution2:
    """
    Intuition:
        Same as Solution1. Just rewritten in a different manner.

    Runtime:
        Same as Solution1.

    Memory:
        Same as Solution1.
    """

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(ix, curr):
            res.append(curr.copy())

            for j in range(ix, len(nums)):
                if j > ix and nums[j] == nums[j - 1]:
                    continue

                curr.append(nums[j])
                dfs(j + 1, curr)
                curr.pop()

        nums.sort()
        dfs(0, [])
        return res
