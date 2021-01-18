# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root):
        result = []
        if root:
            result += self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)
        return result

    def getMinimumDifference(self, root: TreeNode) -> int:
        inorder = self.inorder_traversal(root)
        result = float('inf')
        for node_idx in range(len(inorder) - 1):
            result = min(result, inorder[node_idx + 1] - inorder[node_idx])
        return int(result)


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1, right=TreeNode(3, left=TreeNode(2)))
    print(sol.getMinimumDifference(root))
