from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return -1

        q = deque([root])
        leftmost = root.val
        temp_q = deque([])

        while q:
            node = q.popleft()
            if node.left:
                temp_q.append(node.left)
            if node.right:
                temp_q.append(node.right)
            if not q:
                if temp_q:
                    leftmost = temp_q[0].val
                q = temp_q
                temp_q = deque([])
        return leftmost


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))
    print(sol.findBottomLeftValue(root))
