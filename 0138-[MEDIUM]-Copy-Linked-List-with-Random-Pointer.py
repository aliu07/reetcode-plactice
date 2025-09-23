"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    """
    Intuition:
        The problem can be broken down into two steps. In the first step, we can extend
        the LL by inserting duplicate nodes for each existing node. We can then think of
        the LL as pairs of (original, dupliate) node pairings.

        Then, the second step involves setting the random pointer of the duplicate nodes
        and breaking the LL down into its original and deep copy.

    Runtime:
        O(n) to make duplicates of each node in the LL.

        O(n) to weave the copy list

        Overall, O(n) runtime for the entire solution.

    Memory:
        O(1) auxiliary memory used (excluding the memory allocated for the deep copy).
    """

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # First pass to insert new nodes
        curr = head

        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # Second pass to weave copy list
        curr = head
        res = head.next

        while curr:
            # Ptr to copy node
            copy = curr.next
            # Modify random ptr of copy node
            copy.random = curr.random.next if curr.random else None
            # Shift curr node ptr
            curr = curr.next.next
            # Modify copy node's next ptr
            copy.next = copy.next.next if copy.next else None

        return res
