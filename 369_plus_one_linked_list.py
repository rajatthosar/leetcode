class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(1)
        dummy.next = head

        def add_one(node):
            carry = 0
            if node.next:
                carry = add_one(node.next)
            else:
                node.val += 1
            carry, node.val = divmod(node.val + carry, 10)
            return carry

        carry = add_one(head)
        return dummy.next if carry == 0 else dummy


if __name__ == '__main__':
    sol = Solution()
    root = ListNode(7, ListNode(8, ListNode(9)))
    one_added = sol.plusOne(root)
    result = ''
    while one_added:
        result += str(one_added.val) + '->'
        one_added = one_added.next
    result = result[:-2]
    print(result)
