'''Given the head of a singly linked list, return true if it is a palindrome or false otherwise.'''

# ------ Version 1 -- Create a new reversed list and check if the lists are the same -- O(n) space ------

import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        new_head = copy.deepcopy(head)

        def reverseList(list):
            prev = None
            curr = list

            while curr:

                old_next = curr.next
                curr.next = prev
                prev = curr
                curr = old_next

            return prev

        new_head = reverseList(new_head)

        curr_old, curr_new = head, new_head

        while curr_old:

            if curr_old.val != curr_new.val:
                return False

            curr_old, curr_new = curr_old.next, curr_new.next

        return True


# ------ Version 2 -- Two-pointer approach -- O(1) space ------


def isPalindrome(self, head) -> bool:

    # reverse the list
    def reverseList(list):
        prev = None
        curr = list

        while curr:

            old_next = curr.next
            curr.next = prev
            prev = curr
            curr = old_next

        return prev

    # find the end of the first half
    def find_first_half_end(head):
        slow = head
        fast = head

        # when fast is at the end, slow would be in the middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    first_half_end = find_first_half_end(head)

    # reverse the second hald
    second_half_start = reverseList(first_half_end.next)

    pointer1, pointer2 = head, second_half_start
    res = True

    # compare the two halves
    while res and pointer2:
        if pointer1.val != pointer2.val:
            res = False

        pointer1, pointer2 = pointer1.next, pointer2.next

    return res
