from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([root])
        tempq = []
        while q:
            node = q.popleft()
            if node.left:
                tempq.append(node.left)
            if node.right:
                tempq.append(node.right)
            if not q:
                q = deque(tempq)
                tempq = deque(tempq)
                if tempq:
                    aux_node = tempq.popleft()
                    while tempq:
                        aux_node.next = tempq.popleft()
                        aux_node = aux_node.next
                    aux_node.next = None
        return root


if __name__ == '__main__':
    sol = Solution()
    root = Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6), right=Node(7)))
    print(sol.connect(root))
