# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Intuition:
        The most obvious approach is to use recursion to traverse the binary
        tree.

        Our recursive helper traverses the children of the current node to
        fetch the subtree sum and node count rooted at each child. Then,
        we can compute the sum and node count of the subtree rooted at the
        current node. Finally, we use the information to calculate the
        average and tally nodes whose value is equal to the avg of their
        subtree.

    Runtime:
        O(n) as each node is processed once.

    Memory:
        O(n) for the call stack since we have a skewed tree in the worst case.
    """

    class Solution:
        def averageOfSubtree(self, root: TreeNode) -> int:
            res = 0

            # each call returns total sum and total
            # cnt of nodes of curr subtree
            def dfs(node):
                nonlocal res

                if not node:
                    return 0, 0

                # recurse
                leftSum, leftCnt = dfs(node.left)
                rightSum, rightCnt = dfs(node.right)

                # compute sum and cnt of subtree (which includes curr node)
                totSum = node.val + leftSum + rightSum
                totCnt = 1 + leftCnt + rightCnt

                avg = int(totSum / totCnt)
                if node.val == avg:
                    res += 1

                return totSum, totCnt

            dfs(root)
            return res
