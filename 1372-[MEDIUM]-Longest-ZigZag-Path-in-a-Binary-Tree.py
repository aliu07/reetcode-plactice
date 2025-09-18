from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
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

            if dir == "left":
                dfs(node.right, "right", currLen + 1)
                dfs(node.left, "left", 1)
            else:
                dfs(node.left, "left", currLen + 1)
                dfs(node.right, "right", 1)

        dfs(root.left, "left", 1)
        dfs(root.right, "right", 1)

        return self.maxLen


class Solution2:
    """
    Intuition:
        Same as Solution1

    Runtime:
        Same as Solution1

    Memory:
        Same as Solution1

    Notes:
        Apparently, if we track the results in an array instead of tracking the maxLen
        as a class variable and remove the None check from inside the helper function,
        we get much, much better runtime on the platform.

        This is a trivial change, I just added this because I found it funny.
    """

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        results = []

        def dfs(node, dir, currLen):
            results.append(currLen)

            if dir == "left":
                if node.right:
                    dfs(node.right, "right", currLen + 1)

                if node.left:
                    dfs(node.left, "left", 1)
            else:
                if node.left:
                    dfs(node.left, "left", currLen + 1)

                if node.right:
                    dfs(node.right, "right", 1)

        if not root or (not root.left and not root.right):
            return 0

        if root.left:
            dfs(root.left, "left", 1)

        if root.right:
            dfs(root.right, "right", 1)

        return max(results)
