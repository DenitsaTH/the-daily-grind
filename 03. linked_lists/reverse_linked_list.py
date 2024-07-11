class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:

            # temporarily save the current next node
            old_next = curr.next

            # switch current next to previous
            curr.next = prev

            # new previous is current
            prev = curr

            # new current is the temporarily saved old_next node
            curr = old_next

        return prev
