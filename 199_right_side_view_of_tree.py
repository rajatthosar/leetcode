from collections import deque


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = [root.val]
        queue = deque([root])
        tempq = []
        while queue:
            node = queue.popleft()
            if node.left:
                tempq.append(node.left)
            if node.right:
                tempq.append(node.right)
            if not queue and tempq:
                result.append(tempq[-1].val)
                queue = deque(tempq)
                tempq = []
        return result


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3))
    print(sol.rightSideView(root))
