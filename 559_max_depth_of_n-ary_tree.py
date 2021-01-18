# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0

        if root:
            depth += 1
            if root.children:
                depth += max(self.maxDepth(child) for child in root.children)

        return depth


if __name__ == '__main__':
    node = Node(1, [Node(2, [Node(3, [Node(4)])]), Node(5, [Node(6), Node(7)])])
    sol = Solution()
    print(sol.maxDepth(node))