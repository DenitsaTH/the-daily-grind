'''Given the head of a linked list, remove the nth node from the end of the list and return its head.'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        # maintain the gap between fast and slow -> when fast reaches the end, slow will be just before the Node to remove
        while fast.next:
            fast = fast.next
            slow = slow.next

        # skip the next node
        slow.next = slow.next.next

        return dummy.next
