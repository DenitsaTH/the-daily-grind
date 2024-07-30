'''Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.'''

import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
        
        min, max = -sys.maxsize, sys.maxsize

        def recursive_depth(node=root,min=min, max=max):

            if not node:
                return True
            
            if node.val <= min or node.val >= max:
                return False
    
            left_tree = True
            if node.left:
                left_tree = recursive_depth(node.left, min, node.val)

            right_tree = True
            if node.right:
                right_tree = recursive_depth(node.right, node.val, max)

            return left_tree and right_tree

        return recursive_depth()


tree = TreeNode(2,
                left=TreeNode(1),
                right=TreeNode(3))

print(isValidBST(tree))