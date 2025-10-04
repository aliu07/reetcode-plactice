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
        We somehow want to build the sorted order of the BST so that
        we can peek the kth smallest element in constant time. We can
        use in-order traversal to achieve this.

        This solution takes a recursive approach.

    Runtime:
        Each node needs to be processed and inserted into the inOrder
        array, so O(n) time.

    Memory:
        O(h) for recursive call stack where h is the height of the tree.
        O(log n) best case, O(n) worst case with an unbalanced tree.

        O(n) for the array.

        Overall O(n) memory.
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []

        # in order traversal
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            dfs(node.left)
            inOrder.append(node.val)
            dfs(node.right)

        dfs(root)
        return inOrder[k - 1]
