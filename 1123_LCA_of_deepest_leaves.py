# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        parent_map = dict({root:root})

        def get_depth(node, depth):
            nonlocal max_depth_node_pair,parent_map
            if node:
                if not (node.left or node.right) and max_depth_node_pair[1] < depth:
                    max_depth_node_pair = (node, depth)
                else:
                    if node.left:
                        parent_map[node.left] = node
                    if node.right:
                        parent_map[node.right] = node
                    depth = max(get_depth(node.left, depth + 1), get_depth(node.right, depth + 1))
            return depth
        max_depth_node_pair = (root, 0)
        max_depth = get_depth(root, 0)
        return parent_map[max_depth_node_pair[0]]


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3,
                    left=TreeNode(5,
                                  left=TreeNode(6), right=TreeNode(2,
                                                                   left=TreeNode(7), right=TreeNode(4))),
                    right=TreeNode(1,
                                   left=TreeNode(0), right=TreeNode(8)))
    result = sol.lcaDeepestLeaves(root)
    print(result)
