from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Intuition:
        We can iterate through both lists to create the new list. At the end, we simply
        exhaust list1 or list2 in case their lengths are not equal.

        We use a dummy node here to be able to return the head of the merged list
        efficiently.

    Runtime:
        O(n) since we need to traverse both lists.

    Memory:
        O(n) to build the merged list, but technically O(1) auxiliary space.
    """

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = curr = ListNode()
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = l1
                curr = curr.next
                l1 = l1.next

        while l1:
            curr.next = l1
            curr = curr.next
            l1 = l1.next

        while l2:
            curr.next = l2
            curr = curr.next
            l2 = l2.next

        return dummy.next
