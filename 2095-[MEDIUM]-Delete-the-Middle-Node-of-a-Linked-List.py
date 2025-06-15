from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    """
    Intuition:
        We can use a fast and slow pointer. The idea is that the slow pointer will point to the node that
        we need to remove at the end of the while loop. This implies that we need to keep track of the
        previous node of the slow pointer since we are dealing with a singly linked list.

        We also need a base case to check head.next since we advance by 2 positions for the fast pointer
        in each iteration. Thus, if the list contains only a single node, we just return a None pointer.

    Runtime:
        O(n) -> one pass to traverse the linked list.

    Memory:
        O(1) -> only pointer manipulations in this solution.

    Notes:
        The constraints specify that there is at least a node in the input list.
    """

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not head.next:
            return None

        # Track prev ptr (which is previous node before slow) for
        # ptr rearrangements down the line
        prev, slow, fast = None, head, head

        while fast and fast.next:
            # Advance fast ptr by 2 positions
            fast = fast.next.next

            # Advance slow & prev
            prev = slow
            slow = slow.next

        # Rearrange ptrs
        prev.next = slow.next

        return head

class Solution2:
    """
    Intuition:
        Same general intuition as Solution1. The only tweak we made is rewriting a more
        elegant solution. Instead of having slow point to the node we want to delete at
        the end of the while loop, we make it point to the previous node of the node we
        want to delete.

        Essentially, the slow ptr becomes 'prev' specified in Solution1. This way, we
        remove the need to track an extra pointer. At the end of the while block, we
        do the same pointer manipulations.

    Runtime:
        Same as Solution1

    Memory:
        Same as Solution1

    Notes:
    """

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if not head.next:
            return None

        slow, fast = head, head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next

        return head
