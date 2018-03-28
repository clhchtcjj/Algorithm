# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 判断一棵二叉树是否是对称的
# 思路: 镜像和原树相同的，是对称的

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isSymmetric(root,root)

    def _isSymmetric(self,root1,root2):
        if root1 and root2:
            if root1.val != root2.val:
                return False
            return self._isSymmetric(root1.left,root2.right) and self._isSymmetric(root1.right,root2.left)
        elif not root1 and not root2:
            return True
        else:
            return False

