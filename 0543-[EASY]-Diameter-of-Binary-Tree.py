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
        We essentially need to find the longest path between any 2 nodes
        in the tree. To do this, we can define a function to compute the
        maximum path of its right and left child recursively.

        Note that the diameter does not necessarily include the root.

    Runtime:
        Each node processed once, so O(n) runtime.

    Memory:
        O(1) auxiliary memory.

        O(n) memory for call stack in worst case if tree is unbalanced.

        Overall O(n) memory.
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def findDepth(node):
            if not node:
                return 0

            left = findDepth(node.left)
            right = findDepth(node.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        findDepth(root)

        return self.diameter
