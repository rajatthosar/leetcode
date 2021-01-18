# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> list:
        length = 0
        head = root
        prev = None
        count = i = 0
        result = [None] * k

        while root:
            length += 1
            root = root.next

        if length < k:
            bases = 1
            extras = 0
        else:
            bases = length // k
            extras = length % k

        while head:
            node = ListNode(head.val)
            if extras >= 0:
                if count < bases + 1:
                    if prev:
                        prev.next = node
                else:
                    count = 0
                extras -= 1
            else:
                if count < bases:
                    if prev:
                        prev.next = node
                else:
                    count = 0

            if count == 0:
                result[i] = node
                i += 1
            prev = node
            count += 1
            head = head.next

        return result


if __name__ == '__main__':
    array = [1,2,3,4,5,6,7]
    k = 3
    head = prev = ListNode(array[0])
    for element in array[1:]:
        node = ListNode(element)
        prev.next = node
        prev = node

    sol = Solution()
    print(sol.splitListToParts(head, k))
