# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return ListNode(0)
        elif not l1:
            return l2
        elif not l2:
            return l1

        num1 = l1.val
        num2 = l2.val
        l1 = l1.next
        l2 = l2.next

        while l1 or l2:
            if l1:
                num1 *= 10
                num1 += l1.val
                print(num1)
                l1 = l1.next

            if l2:
                num2 *= 10
                num2 += l2.val
                print(num2)
                l2 = l2.next

        result = num1 + num2
        next = None

        while result > 0:
            digit = result % 10
            result //= 10
            node = ListNode(digit)
            if not next:
                next = node
                node.next = None
            else:
                node.next = next
                next = node

        return node


if __name__ == '__main__':
    nums1 = [7, 2, 4, 3]
    nums2 = [5, 6, 4]

    def get_ll_from_list(nums):
        head = None
        prev = None

        for number in nums:
            node = ListNode(number)
            if not head:
                head = node
                prev = head
            else:
                prev.next = node
                prev = node
        return head

    head1 = get_ll_from_list(nums1)
    head2 = get_ll_from_list(nums2)

    sol = Solution()
    print(sol.addTwoNumbers(head1,head2))