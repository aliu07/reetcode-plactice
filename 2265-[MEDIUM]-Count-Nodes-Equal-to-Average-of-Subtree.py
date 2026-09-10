# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
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


class Solution2:
    """
    Intuition:
        Use an iterative DFS approach. We use the subtree dictionary to propagate the
        subtree sums and node counts and an explicit stack. We use post-order traversal
        as a node's total sum and node count (used to compute avg) requires knowing the
        sum and node count for its children first.

    Runtime:
        O(2n) ~ O(n) as each node needs to be processed twice.

    Memory:
        O(n) for the stack.

        O(n) for the subtree.

        Overall, O(n) memory.

    """

    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, False)]
        # maps node -> (sum, node count)
        subtree = {}

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if not visited:
                # revisit node after processing children
                stack.append((node, True))
                # push children onto stack
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                leftSum, leftCnt = subtree.get(node.left, (0, 0))
                rightSum, rightCnt = subtree.get(node.right, (0, 0))

                totSum = node.val + leftSum + rightSum
                totCnt = 1 + leftCnt + rightCnt

                avg = totSum // totCnt

                if node.val == avg:
                    res += 1

                subtree[node] = (totSum, totCnt)

        return res
