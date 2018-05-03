# -*- coding: utf-8
__author__ = 'CLH'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            root = node
            return root
        else:
            return self._addOneRow(root,v,d)

    def _addOneRow(self, root, v, d):
        if not root:
            return root
        if d == 2:
            if root.left:
                node = TreeNode(v)
                node.left = root.left
                root.left = node
            else:
                root.left = TreeNode(v)
            if root.right:
                node = TreeNode(v)
                node.right = root.right
                root.right = node
            else:
                root.right = TreeNode(v)
            if not root.left and not root.right:
                root.left = TreeNode(v)
                root.right = TreeNode(v)
        root.left = self.addOneRow(root.left,v,d-1)
        root.right = self.addOneRow(root.right,v,d-1)
        return root
