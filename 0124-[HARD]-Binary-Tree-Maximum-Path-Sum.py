from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Intuition:
        The maximum path sum can be found by considering all possible combinations
        of paths. Each node can either be the start of the path, somewhere in the
        middle of the path or the end of the path.

        We can use a depth-first search (DFS) approach to traverse the tree and
        calculate the maximum path sum at each node.

        At each node, we calculate the maximum path sum that includes the node as
        the start, middle or end of the path. We then update the maximum path sum
        seen so far.

        Note: this solution was written without consulting the solution... it can
        be polished further.

    Runtime:
        Each node is processed once in a bottom-up manner. Therefore, we have
        a linear runtime of O(n).

    Memory:
        Call stack requires O(h) where h is the height of the tree. In the
        best case, h is log(n). In the worst case h is n with an unbalanced
        tree.

        Overall O(n) memory.
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -inf

        def dfs(node):
            if not node:
                return -inf

            left = dfs(node.left)
            right = dfs(node.right)

            combinations = [
                left,
                right,
                node.val,
                left + node.val,
                right + node.val,
                left + node.val + right,
            ]
            highest = max(combinations)

            if highest > self.maxSum:
                self.maxSum = highest

            return max([left + node.val, right + node.val, node.val])

        dfs(root)
        return int(self.maxSum)
