# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def helper(self, s, t):
        if s is None and t is None:
            return True
        elif s is not None and t is not None:
            return s.val == t.val and self.helper(s.left, t.left) and self.helper(s.right, t.right)
        else:
            return False

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.helper(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(1)
    head.right = TreeNode(2)
    target = TreeNode(1)

    sol = Solution()

    print(sol.isSubtree(head, target))
