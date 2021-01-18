from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


if __name__ == '__main__':
    # tree builder
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    ret_root = sol.lowestCommonAncestor(root=root, p=TreeNode(5), q=TreeNode(4))

    # printer
    result = [[ret_root.val]]
    q = deque([ret_root])
    tempq = []
    valq = []
    while q:
        node = q.popleft()
        if node.left:
            tempq.append(node.left)
            valq.append(node.left.val)
        if node.right:
            tempq.append(node.right)
            valq.append(node.right.val)
        if not q:
            result.append(valq)
            valq = []
            q = deque(tempq)
            tempq = []
    print(result)
