from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Intuition:
        This problem is fairly straightforward. He simply use either BFS or DFS to
        process each node in the binary tree and determine if its depth is the
        greatest.

    Runtime: O(n) where n is the number of nodes in the binary tree

    Memory: O(n) where n is the number of nodes in the binary tree
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Encode as (node, depth)
        q = deque([(root, 1)])
        maxDepth = 0

        while q:
            node, depth = q.popleft()

            if depth > maxDepth:
                maxDepth = depth

            if node.left:
                q.append((node.left, depth + 1))

            if node.right:
                q.append((node.right, depth + 1))

        return maxDepth
