'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        curr1, curr2 = list1, list2
        curr_dummy = dummy

        while curr1 or curr2:

            if not curr1:
                curr_dummy.next = curr2
                return dummy.next

            if not curr2:
                curr_dummy.next = curr1
                return dummy.next

            if curr1.val <= curr2.val:

                curr_dummy.next = curr1
                curr1 = curr1.next
                curr_dummy = curr_dummy.next

            else:
                curr_dummy.next = curr2
                curr_dummy = curr_dummy.next
                curr2 = curr2.next

        return dummy.next
