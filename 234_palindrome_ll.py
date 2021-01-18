class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        array = []

        while head:
            array.append(head.val)
            head = head.next

        init_ptr = 0
        tail_ptr = len(array) - 1

        while init_ptr < tail_ptr:
            if array[init_ptr] != array[tail_ptr]:
                return False
            init_ptr += 1
            tail_ptr -= 1
        return True


if __name__ == '__main__':
    sol = Solution()
    node = ListNode(-129, ListNode(-129))
    print(sol.isPalindrome(node))
