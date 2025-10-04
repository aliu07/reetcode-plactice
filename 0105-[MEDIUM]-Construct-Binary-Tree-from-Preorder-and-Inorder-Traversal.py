from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Intuition:
        For the preorder array, we know that the first element is the immediate
        next node. In in-order traversal, we only process the node the second
        time we see it.

        Using this information, we can recrusively construct the tree by peeking
        the first element in the preorder array, searching the respective index
        of that element in the inorder array, use that mid index to divide the
        preorder and inorder arrays, and pass down the divided arrays into the
        recursive call.

        The preorder array can be visualized like so:
            <current node> | <left subtree elmts> | <right subtree elmts>

        The inorder array can be visualized like so:
            <left subtree elmts> | <current node> | <right subtree elmts>

        Thus, with the mid index, we can partition both arrays appropriately.

    Runtime:
        Process each element in the traversal arrays -> O(n).

        Find the mid index within the inorder array -> O(n). However, this is
        needed at every single function call (there are n function calls, one
        for each elmt).

        Slicing the preorder/inorder arrays into subarrays takes O(n) time.
        This step is also repeated at every single function call.

        Overall, O(n^2).

    Memory:
        O(h) for the call stack -> O(n) in the worst case with an unbalanced tree.
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root
