from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Intuition:
        If you have ever done binary addition, the solution is straightforward. We keep track
        of the carry and iterate so long as we either have node values in l1, l2 or have
        carry-over we need to account for.

    Runtime:
        O(n) where n is the length of the longest linked list between l1 and l2.

    Memory:
        O(n) to store the resulting linked list. Technically O(1) auxiliary space.
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry
            carry = 1 if sum >= 10 else 0
            remainder = sum % 10

            curr.next = ListNode(remainder)
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
