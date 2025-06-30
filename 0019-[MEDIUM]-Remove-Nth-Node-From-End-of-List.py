from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Intuition:
        Like with many linked list problems, we can employ a fast and slow pointer. We offset the fast pointer first
        and then use the slow pointer to target the nth node in the linked list.

        We need to account for a special case where the target node to be deleted is the head of the list, hence why
        we check if fast is not None after offsetting it in the first loop.

    Runtime:
        O(N) since we need 1 pass.

    Memory:
        O(1) since we are only using pointers.
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        for i in range(n):
            fast = fast.next

        # Cover case where we need to remove head
        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
