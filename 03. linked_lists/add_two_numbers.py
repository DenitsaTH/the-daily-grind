'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        new_l = ListNode()
        current = new_l
        remainder = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            curr_sum = x + y + remainder
            remainder = curr_sum // 10
            new_val = curr_sum % 10

            current.next = ListNode(new_val)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if remainder > 0:
            current.next = ListNode(remainder)

        return new_l.next
