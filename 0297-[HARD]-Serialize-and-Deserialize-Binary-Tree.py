from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """
    Encodes a tree to a single string.

    Intuition:
        The solution uses a recursive DFS approach while relying on pre-order
        traversal to serialize the binary tree. The serialized string is
        constructed by appending the value of each node followed by a comma.
        A special string is used to represent null nodes.

    Runtime:
        Each node needs to be processed once, meaning O(n) runtime.

    Memory:
        The recursive call stack can go as deep as the height of the tree,
        which is O(log n) for a balanced tree and O(n) for a skewed tree.
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("null")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    """
    Decodes your encoded data to tree.

    Intuition:
        The solution uses a recursive DFS approach while relying on pre-order
        traversal to deserialize the binary tree. The serialized string is
        split into a list of values, and a pointer is used to keep track of
        the current position in the list. If the current value is "null",
        the pointer is incremented and None is returned. Otherwise, a new
        TreeNode is created with the current value, and the left and right
        subtrees are deserialized recursively.

    Runtime:
        Each node needs to be processed once, meaning O(n) runtime.

    Memory:
        The recursive call stack can go as deep as the height of the tree,
        which is O(log n) for a balanced tree and O(n) for a skewed tree.
    """

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "null":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
