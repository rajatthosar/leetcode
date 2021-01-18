from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        result = []
        queue = deque([root])
        secondary_q = deque([])
        addition = 0
        counter = 0

        while queue:
            node = queue.popleft()
            addition += node.val
            counter += 1

            if node.left:
                secondary_q.append(node.left)
            if node.right:
                secondary_q.append(node.right)

            if not queue:
                result.append(addition / counter)
                addition = 0
                counter = 0
                queue = secondary_q
                secondary_q = deque([])

        return result


if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(3, TreeNode(9), TreeNode(20))
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    print(sol.averageOfLevels(tree))