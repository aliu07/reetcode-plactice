# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Intuition:
        Build a dictionary where the key is the level and the value
        is an array contaning all nodes at that level. This solution
        illustrates a recursive approach.

    Runtime:
        Each node is processed at most once -> O(n) runtime.

    Memory:
        Call stack is O(h) memory where h is the height of the tree.
        In the worst case, the height is 'n' if we have an unbalanced
        tree.

        Dictionary is also O(n) since we store information about all
        nodes in it.

       Thus, overall memory complexity is O(n).
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)

        def dfs(node, lvl):
            if not node:
                return

            levels[lvl].append(node.val)

            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)

        dfs(root, 0)
        return list(levels.values())
