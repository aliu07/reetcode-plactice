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


class Solution2:
    """
    Intuition:
        We can make our algorithm slightly more memory efficient by
        removing the inOrder array.

        Instead, we store k in a nonlocal var and decrement it. Once
        it hits 0, we know we hit our kth smallest elmt so that beocmes
        our result.

        This solution still takes a recursive approach.

    Runtime:
        O(n) -> same as Solution1.

    Memory:
        Removed the need for the array, but call stack is still
        O(n) in the worst case.

        Overall, O(n) memory.

    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.k = k

        # in order traversal
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            dfs(node.left)

            self.k -= 1
            if self.k == 0:
                self.res = node.val

            dfs(node.right)

        dfs(root)
        return self.res


class Solution3:
    """
    Intuition:
        Same idea as Solution1, but we use an iterative approach with an array
        to simulate the call stack while still respecting an in order traversal.

    Runtime:
        O(n) -> same as Solution1 (consider the case where k == number of nodes
        in tree).

    Memory:
        O(n) -> same as Solution1, stack array can be linear if tree is unbalanced.
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = root
        stack = []

        while True:
            # traverse left until hit a dead end
            if node:
                stack.append(node)
                node = node.left
            # in order processing
            else:
                node = stack.pop()

                k -= 1
                if k == 0:
                    return node.val

                if node.right:
                    node = node.right
                else:
                    node = None
