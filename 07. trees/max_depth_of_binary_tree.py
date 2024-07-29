'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):

        def recursive_depth(depth=1, node=root):

            if not node:
                return 0

            if not node.right and not node.left:
                return depth

            depth += 1

            right = recursive_depth(depth, node.right)
            left = recursive_depth(depth, node.left)

            return right if right > left else left

        return recursive_depth()
