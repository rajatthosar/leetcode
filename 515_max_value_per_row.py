from collections import deque

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = deque([root])
        result = [root.val]
        tempq = deque([])
        max_val = float('-inf')

        while q:
            node = q.popleft()
            if node.left:
                tempq.append(node.left)
                max_val = max(max_val, node.left.val)
            if node.right:
                tempq.append(node.right)
                max_val = max(max_val, node.right.val)
            if not q:
                if max_val > float('-inf'):
                    result.append(max_val)
                max_val = float('-inf')
                q = tempq
                tempq = deque([])
        return result


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))
    print(sol.largestValues(root))
