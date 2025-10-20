from typing import List


class Solution:
    """
    Intuition:
        We use a recursive backtracking approach where we keep track of the
        current starting index and the current subset being constructed. At
        each step, we can either include or exclude the next number in the
        subset. If we include, we extend the subset, if we exclude, we ess-
        entially terminate the current subset.

        Our overall termination condition is when the starting index exceeds
        the length of the input array.

        We also only juggle a single reference to 'curr' to be more efficient.

    Runtime:
        There are 2^n possible subsets for an input array of length n.

        The largest subset is of size n.

        Thus, the overall runtime is O(n * 2^n).

    Memory:
        The depth of our recursion tree is at most n.

        We need O(n) space at most to store the largest subset.

        We need O(2^n) space to store all subsets.

        Thus, the overall memory is bounded by O(n) auxiliary space or O(n * 2^n)
        total.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(ix, curr):
            # ix goes beyond arr
            if ix >= len(nums):
                return

            # record curr subset
            res.append(curr.copy())

            # explore further choices
            for j in range(ix + 1, len(nums)):
                curr.append(nums[j])  # choose elmt
                dfs(j, curr)  # explore
                curr.pop()  # backtrack

        dfs(-1, [])
        return res
