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
        We need to traverse the tree while encoding the direction somehow
        to ensure that we satisfy the properties of a zigzag. To do this,
        we can use a recursive approach where we pass in the current node,
        the current direction of travel, and the current length.

        This way, we have 2 subcases for direction: left and right. For
        each, we need to check if we can extend the current zigzag or if
        we need to start a new zigzag with the current node as the source.

    Runtime:
        O(log n) on average where log n represents the height of the tree
        and O(n) if the tree is skewed.

    Memory:
        Same idea as runtime. O(log n) on average, O(n) in the worst case.
    """

    maxLen = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node, dir, currLen):
            if not node:
                return

            self.maxLen = max(currLen, self.maxLen)

            if dir == 'left':
                dfs(node.right, 'right', currLen + 1)
                dfs(node.left, 'left', 1)
            else:
                dfs(node.left, 'left', currLen + 1)
                dfs(node.right, 'right', 1)

        dfs(root.left, 'left', 1)
        dfs(root.right, 'right', 1)

        return self.maxLen
