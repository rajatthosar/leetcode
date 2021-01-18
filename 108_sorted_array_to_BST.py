# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if not nums:
            return

        med = len(nums) // 2
        root = TreeNode(nums[med])
        if med == 0:
            root.left = self.sortedArrayToBST(nums[:med])
        else:
            root.left = self.sortedArrayToBST(nums[:med])
            root.right = self.sortedArrayToBST(nums[med + 1:])

        return root


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9, 8]
    sol = Solution()
    root = sol.sortedArrayToBST(nums)
    print(root)
