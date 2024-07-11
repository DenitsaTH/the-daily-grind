'''There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Remove the current node from the linked list.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):

        # get next node's value (there will be next, we know this node is not the tail)
        next_val = node.next.val

        # switch the current node's next to the next node's next
        node.next = node.next.next

        # switch the current node's value with next_val
        node.val = next_val
