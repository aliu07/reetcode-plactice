# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Intuition:
        We will start with a brute force approach. We transform the linked list into
        an array so we can process it sequentially more efficiently.

       We start by iterating over windows of size k. If the window size is less than
       k, we break. Otherwise, we reverse the elements.

       Then, we reconstruct the linked list given the processed array.

    Runtime:
        O(n) to transform the linked list into array form.

        O(n) to reverse the k-groups in the array.

        O(n) to rebuild the linked list.

        Overall runtime is O(n).

    Memory:
        O(n) to store the nodes in an array.
    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # store each node as an element in an array
        curr, arr = head, []
        while curr:
            arr.append(curr)
            curr = curr.next

        # reverse by k-group
        for l in range(0, len(arr), k):
            r = l + k - 1

            # if we have less elements than k
            if r >= len(arr):
                break

            while l < r:
                n1, n2 = arr[l], arr[r]
                arr[l] = n2
                arr[r] = n1

                l += 1
                r -= 1

        # build resulting linked list
        dummy = curr = ListNode()
        for i in range(len(arr)):
            curr.next = arr[i]
            curr = curr.next
        # terminate the list!
        curr.next = None

        return dummy.next
