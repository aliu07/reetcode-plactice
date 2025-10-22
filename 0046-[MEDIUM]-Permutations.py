from typing import List


class Solution:
    """
    Intuition:
        We can use DFS to backtrack.

        Our base case is when the current permutation has reached
        the same length as the input array.

        At each recursive step, we add a number that is not
        currently in our permutation.

        We can afford to iterate through all numbers to find missing
        ones because the nums array is bounded at size 6.

    Runtime:
        Copying a permutation takes O(n).

        There are n! permutations in total.

        Thus, we have O(n * n!) runtime overall.

    Memory:
        Call stack depth is O(n) space.

        Permutation array 'curr' takes O(n) space.

        Overall O(n) auxiliary space (excluding res).
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())

            for n in nums:
                if n not in curr:
                    curr.append(n)
                    dfs(curr)
                    curr.pop()

        dfs([])
        return res
