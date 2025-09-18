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
        Searching for the existence of the key value in a BST is trivial. The hard part
        of this problem is figuring out how to delete the target node if found. Mainly,
        we need to keep in mind the properties of a BST: every element in the left
        subtree has to be lesser than the current node and every element in the right
        subtree has to be greater than the current node.

        With these properties in mind, we realize intuitively that we need to rotate
        in a node that preserves them. Simply, we can choose the smallest element in
        the right subtree to take the place of our deleted node. By doing so, we still
        guarantee that every element in the left subtree will be smaller, but also that
        every element in the right subtree will be greater than the new node's value.

    Runtime:
        In the worst case, our tree will be skewed (i.e. a linked list) and so the
        runtiem will be O(n). However, the average runtime will be O(log n) or the
        height of the BST.

    Memory:
        Each recursive call takes memory on the call stack. We have one call per
        level of the BST, so the total number of calls represents the height of the
        tree. In the worst case, the tree is skewed which gives a memory complexity
        of O(n). On average, we will have O(log n) calls.
    """

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Target node maybe in left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # Target node maybe in right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # Target node found
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = self.getMin(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)

        return root

    # Helper function to find the next successor
    # The successor is always the smallest node in the right subtree
    def getMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left

        return node
