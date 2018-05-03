# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 思路：先遍历右子树-> 根 -> 左子树 ，保留上一节点的值
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        lastsum = [0]
        self._converyBST(root,lastsum)
        return root

    def _converyBST(self,node,lastsum):
        if not node:
            return
        self._converyBST(node.right,lastsum)
        node.val += lastsum[0]
        lastsum[0] = node.val
        self._converyBST(node.left,lastsum)

