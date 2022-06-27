from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def createLinkFromList(list: List):
        head: ListNode = None
        current: ListNode = None
        for i, v in enumerate(list):
            next = ListNode(v)
            if i == 0:
                head = next
                current = next
            if (current is not None):
                current.next = next
                current = next

        return head


class Solution:
    def reversePrint(head: ListNode) -> List[int]:
        values = []
        node: ListNode = head
        while node is not None:
            values.append(node.val)
            node = node.next

        ret = reversed(values)
        for i, v in enumerate(ret):
            print(v)

        return ret


if (__name__ == '__main__'):
    Solution.reversePrint(
        ListNode.createLinkFromList([1, 2, 3, 4, 5])
    )
