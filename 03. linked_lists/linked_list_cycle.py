'''Given head, the head of a linked list, determine if the linked list has a cycle in it.
Return true if there is a cycle in the linked list. Otherwise, return false.'''

from test_funcs import createLinkedList

# ------ Version 1 -- Use set() to keep track of already passed Nodes -- O(n) space ------

class Solution:
    def hasCycle(self, head):
        s = set()
        curr = head

        while curr:

            if curr in s:
                return True

            if curr not in s:
                s.add(curr)

            curr = curr.next

        return False


# ------ Version 2 -- Two-pointer approach -- O(1) space ------

def hasCycle(head):

    if not head or not head.next:
        return False
    
    fast = slow = head

    while fast and fast.next:

        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            return True

    return False


# Test

lst = createLinkedList([1], -1)
print(hasCycle(lst))
