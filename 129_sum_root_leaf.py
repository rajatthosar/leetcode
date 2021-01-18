class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0

    def sumNumbers(self, root: TreeNode) -> int:
        path = 0

        def path_sum(root, path):
            if root:
                path *= 10
                path += root.val
                if not (root.left or root.right):
                    self.result += path
                else:
                    path_sum(root.left, path)
                    path_sum(root.right, path)

        path_sum(root, path)
        return self.result


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(sol.sumNumbers(root))
