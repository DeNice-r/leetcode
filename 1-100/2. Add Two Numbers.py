from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_int(cls, value: int):
        root = ListNode(value % 10)
        value //= 10
        node = root

        while value > 0:
            node.next = ListNode(value % 10)
            value //= 10
            node = node.next

        return root

    def __str__(self):
        r = ''
        node = self
        while node is not None:
            r = str(node.val) + r
            node = node.next

        return r

    def __repr__(self):
        return self.__str__()

    # Realistic solution through add operator implementation
    def __add__(self: Optional['ListNode'], other: Optional['ListNode']) -> Optional['ListNode']:
        r = ListNode()
        node, node1, node2 = r, self, other
        surplus = 0

        while node1 or node2:
            node.next = ListNode((node1.val if node1 else 0) + (node2.val if node2 else 0) + surplus)
            node, node1, node2 = node.next, node1 and node1.next, node2 and node2.next
            surplus = node.val // 10
            node.val -= surplus * 10

        if surplus:
            node.next = ListNode(surplus)

        return r.next


# First solution
# def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     r = ListNode((l1.val if l1 else 0) + (l2.val if l2 else 0))
#     node = r
#     surplus = r.val // 10
#     node.val -= surplus * 10
#     node1, node2 = l1.next, l2.next
#
#     while node1 or node2:
#         node.next = ListNode((node1.val if node1 else 0) + (node2.val if node2 else 0) + surplus)
#         node, node1, node2 = node.next, node1 and node1.next, node2 and node2.next
#         surplus = node.val // 10
#         node.val -= surplus * 10
#
#     if surplus:
#         node.next = ListNode(surplus)
#
#     return r


# # Better solution without copy of while body in the preparation block
# def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     r = ListNode()
#     node, node1, node2 = r, l1, l2
#     surplus = 0
#
#     while node1 or node2:
#         node.next = ListNode((node1.val if node1 else 0) + (node2.val if node2 else 0) + surplus)
#         node, node1, node2 = node.next, node1 and node1.next, node2 and node2.next
#         surplus = node.val // 10
#         node.val -= surplus * 10
#
#     if surplus:
#         node.next = ListNode(surplus)
#
#     return r.next


chain1 = ListNode.from_int(500)
chain2 = ListNode.from_int(500)
# chain1 = ListNode.from_int(255)
# chain2 = ListNode.from_int(145)

print()
print(f'{chain1} + {chain2} = {chain1 + chain2}')
