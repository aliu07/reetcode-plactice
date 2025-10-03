# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Intuition:
        We solve this problem in 3 steps:

        1. Find all the parent relations of all nodes in the tree. We can
        terminate this step early if we have seen both p and q.

        2. Build a hashset containing all the ancestors of p.

        3. Iterate over the ancestors of q until we hit a common one with p.

    Runtime:
        Each node is processed at most once to define their parent mapping.
        In the worst case, we need to process all nodes before p and q are
        processed, leading to O(n) time.

        Fetching all the ancestors of p into a hashset takes O(n) at worst.

        Iterating over q until we hit a common ancestor also take O(n) time
        at worst.

        Overall, O(n) time.

    Memory:
        Stack takes up at most O(h) where h is height of tree. In best
        case, h is log n where n is the number of nodes. In the worst
        case, h is n if we have an unbalanced tree.

        The parent hashmap takes up linear space.

        Overall O(n).
    """

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if not root:
            return None

        # pattern: need to map ancestor of each node
        parent_map = {root: None}
        stack = [root]  # mirrors call stack

        while p not in parent_map or q not in parent_map:
            node = stack.pop()

            if node.left:
                parent_map[node.left] = node  # type: ignore
                stack.append(node.left)

            if node.right:
                parent_map[node.right] = node  # type: ignore
                stack.append(node.right)

        ancestors_p = set()
        while p:
            ancestors_p.add(p)
            p = parent_map[p]  # type: ignore

        while q not in ancestors_p:
            q = parent_map[q]

        return q
