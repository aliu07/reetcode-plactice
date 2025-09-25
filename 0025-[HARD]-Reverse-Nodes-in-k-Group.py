# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
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


class Solution2:
    """
    Intuition:


    Runtime:
        Getting kth node takes at worst O(n).

        Rearranging ptrs takes O(n) too, every node is reversed
        at most once. Linking groups takes O(1) time.

        Overall O(n) time.

    Memory:
        O(1) by removing the array and solely maniuplating ptrs.
    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base cases
        if not head or k == 1:
            return head

        # need dummy node to return head
        # head will change since we are reversing groups
        dummy = ListNode(0, head)
        # groupPrev = last node in the previous group
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)

            # don't have enough remaining nodes to form a k-group
            if not kth:
                break

            groupNext = kth.next  # starting node of next group

            # reverse current group
            #
            # note how prev is initialized to groupNext
            # we link current head (which will become last node
            # once we reverse to the first node of the next group)
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                curr, prev = tmp, curr

            # store first node of current group
            tmp = groupPrev.next
            # link last node of prev group to kth node
            # of current group
            groupPrev.next = kth
            # set new groupPrev to last node of current group
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr
