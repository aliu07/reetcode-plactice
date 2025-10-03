# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Intuition:
        We can rely on the properties of a BST to reduce our search space.

        If the value of the node we are currently at is greater than both
        p and q, then we know that both of them are located in the left
        subtree and can go down a level.

        If the value of the node we are currently at is less than both p
        and q, then we know that both of them are located in the right
        subtree and can go down a level as well.

        Finally, if the value of the node we are currently at falls some-
        where in between p and q, then we know that we have the lowest
        commont ancestor.

    Runtime:
        At each step, we go down a level in the BST. Thus, runtime is O(h)
        where h is the height of the tree. In the best case, h is log n. In
        the worst case, h is n where we have an unbalanced tree.

    Memory:
        O(h) as well for call stack. Best case O(log n), worst case O(n).
    """

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
