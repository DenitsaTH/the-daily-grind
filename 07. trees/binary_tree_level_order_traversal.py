'''Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            level_values = []

            for _ in range(level_size):
                node = q.popleft()
                level_values.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level_values)

        return res
