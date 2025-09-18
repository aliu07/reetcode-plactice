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
        We are given a binary search tree. Knowing properties of a BST, we can
        define subcases depending on if the target value is greater than, equal
        to or less than the value of the current node.

    Runtime: O(log n) since we go down one level at each step and there are at
             most log n levels to the tree

    Memory: O(1)
    """

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if val < root.val:
                root = root.left
            elif root.val == val:
                return root
            else:
                root = root.right

        return None
