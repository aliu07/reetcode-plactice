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
        List all values using in-order traversal DFS. Then, we can
        construct the binary search tree using a divide and conquer
        approach. At each step, we maintain left and right bounds
        for the current subtree we are constructing.

    Runtime:
        Each node is processed once during the in-order traversal,
        so O(n).

        Then, we iterate over each node to build the new BST, so
        O(n).

        Overall, O(n) runtime.

    Memory:
        O(n) for the array to store the sorted order of nodes.

        O(n) for the balanced BST.

        Overall, O(n) space.
    """

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # in-order traversal to get ordering
        nodes = []

        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            nodes.append(node.val)
            in_order_traversal(node.right)

        # construct_bst new balanced bst from sorted vals
        def construct_bst(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            node = TreeNode(nodes[mid])
            node.left = construct_bst(l, mid - 1)
            node.right = construct_bst(mid + 1, r)

            return node

        in_order_traversal(root)
        return construct_bst(0, len(nodes) - 1)
