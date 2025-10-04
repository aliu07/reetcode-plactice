from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
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


class Solution2:
    """
    Intuition:
        We use the same recursive approach as before, but introduce
        two key optimizations to achieve linear runtime.

        First, we build a hashmap to store each value’s index in the
        inorder array, allowing O(1) lookups instead of scanning for
        the root’s position each time.

        Second, we avoid costly list slicing by using left and right
        index bounds (l, r) to represent the current inorder subarray.
        This way, recursion operates directly on index ranges while
        a single preorder pointer (self.preIx) tracks the current root
        node across calls.

    Runtime:
        One pass over elmts in the arrays -> O(n).

        Removed the extra factor of n by using hashmap to store indices.

        Also removed extra factor of n by using l, r bounds instead of
        slicing subarrays.

        Overall O(n).

    Memory:
        O(n) for hashmap.

        O(h) for call stack -> O(n) worst case with unbalanced tree.

        Overall, still O(n).
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIx = 0
        indices = {val: ix for ix, val in enumerate(inorder)}

        def dfs(l, r):
            if l > r:
                return None

            root = TreeNode(preorder[self.preIx])
            self.preIx += 1

            mid = indices[root.val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(preorder) - 1)
