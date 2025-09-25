# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Intuition:
        Use a recursive approach. We process each node and
        recursively call the function on its children.

    Runtime:
        Need to process each node to invert children, so
        runtime of O(n).

    Memory:
        O(1) auxiliary space, so constant memory solution.

        Although note that call stack is O(log n) in the
        best case for a balanced binary tree (root to leaf
        path is log n) and O(n) in the worst case for an
        unbalanced tree.
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
