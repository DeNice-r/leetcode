class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        length = 1
        while node.next is not None:
            length += 1
            node = node.next
        if length == 1:
            return None
        unt_del = length - n - 1
        node = head
        while unt_del > 0:
            unt_del -= 1
            node = node.next
        if n == 0:
            node.next = None
        else:
            node.next = node.next.next
        return head
