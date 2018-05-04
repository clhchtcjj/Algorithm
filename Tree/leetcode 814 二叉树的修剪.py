# -*- coding:utf-8 -*-
__author__ = 'CLH'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        # print left,right
        if root.val == 0 and not left and not right:
            root = None
        else:
            root.left = left
            root.right = right
        return root