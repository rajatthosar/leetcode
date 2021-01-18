import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.linked_list_vals = []
        while head:
            self.linked_list_vals.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return self.linked_list_vals[random.randint(0, len(self.linked_list_vals) - 1)]


if __name__ == '__main__':
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    sol = Solution(linked_list)
    print(sol.getRandom())
    print(sol.getRandom())
    print(sol.getRandom())
    print(sol.getRandom())
    print(sol.getRandom())
    print(sol.getRandom())
