class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current

    if pos != -1:
        current.next = cycle_node

    return head
