# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Intuition:
        Recursive approach. At each node, check if each child's
        subtree is balanced. We return a boolean and the max
        height of the respective subtree at each recursive call.

    Runtime:
        Each node processed once, so O(n) runtime.

    Memory:
        Call stack takes O(n) in worst case where we have
        unbalanced tree. Therefore, overall memory is O(n).
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, 0

            balL, hL = dfs(node.left)
            balR, hR = dfs(node.right)
            balanced = balL and balR and abs(hL - hR) <= 1

            return balanced, 1 + max(hL, hR)

        isBalanced, _ = dfs(root)
        return isBalanced
