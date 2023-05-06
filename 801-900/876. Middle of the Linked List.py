# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from math import ceil


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        length = 1

        while node.next is not None:
            length += 1
            node = node.next
        mid = ceil((length - 1) / 2)

        node = head
        while mid > 0:
            mid -= 1
            node = node.next
        return node