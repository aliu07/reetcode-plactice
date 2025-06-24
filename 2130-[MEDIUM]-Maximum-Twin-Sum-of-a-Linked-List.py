from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    """
    Intuition:
        Since we cannot index efficiently in a linked list, we map the linked list
        to an array to be able to access different indices efficiently. This way,
        we can pass through the array to compute all the twin sums are return the
        max.

    Runtime:
        O(n) -> dominated by traversal of input linked list.

    Memory:
        O(n) -> dominated by size of linked list.
    """

    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        sums = []

        for i in range(len(nums) // 2):
            sums.append(nums[i] + nums[-1 - i])

        return max(sums)
