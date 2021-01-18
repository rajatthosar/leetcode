from collections import deque

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return [[""]]
        q = deque([root])
        levels = 0
        tempq = []
        while q:
            node = q.popleft()
            if node.left:
                tempq.append(node.left)
            if node.right:
                tempq.append(node.right)
            if not q:
                levels += 1
                q = deque(tempq)
                tempq = []