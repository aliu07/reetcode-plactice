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


class Solution2:
    """
    Intuition:
        Iterative approach. The idea is the same, but we try simulating
        the call stack using a stack array within our solution.

    Runtime:
        Each node requires constant work, so O(n) runtime also.

    Memory:
        Also O(n) overall since we mirror call stack with a data structure.
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        node = root  # current node
        last = None  # last fully processed node
        stack = []  # simulate call stack
        depths = {}  # { node: depth }

        while stack or node:
            # travel down left subtree as far as possible
            if node:
                stack.append(node)
                node = node.left
            # hit bottom of left subtree
            else:
                # peeking the top of the stack (potential parent)
                node = stack[-1]

                # if curr node does not have right child
                # or right child fully processed
                if not node.right or node.right == last:
                    stack.pop()

                    hL = depths.get(node.left, 0)
                    hR = depths.get(node.right, 0)

                    # check balance
                    if abs(hL - hR) > 1:
                        return False

                    # add current node's depth
                    depths[node] = max(hL, hR) + 1

                    # node is now fully processed
                    last = node
                    # set current node to None so we have to pop stack
                    # on next iter
                    node = None
                # right child not fully processed
                else:
                    node = node.right

        return True
