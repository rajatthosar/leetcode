from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False

        q = deque([root])
        tempq = []
        val_q = []

        while q:
            node = q.popleft()
            if node.left:
                tempq.append(node.left)
                val_q.append(node.left.val)
            if node.right:
                tempq.append(node.right)
                val_q.append(node.right.val)
            val_q.append(-1)
            if not q:
                init_idx = diff_idx = last_idx = None
                val_idx = 0
                while val_idx < len(val_q):
                    if init_idx is None and val_q[val_idx] in [x, y]:
                        init_idx = val_idx
                    elif val_q[val_idx] == -1:
                        diff_idx = val_idx
                    elif init_idx is not None and val_q[val_idx] in [x, y]:
                        last_idx = val_idx
                    if init_idx is not None and \
                            diff_idx is not None and \
                            last_idx is not None and \
                            init_idx < diff_idx < last_idx:
                        return True
                    val_idx += 1
                val_q = []
                q = deque(tempq)
                tempq = []
        return False


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5)))
    print(sol.isCousins(root, 4, 5))
