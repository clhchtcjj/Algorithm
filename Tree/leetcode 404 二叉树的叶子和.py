# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 思路：对左叶子节点求和,利用一个flag，标记是否是左叶子
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum = [0]
        if root.left:
            self._sumOfLeftLeaves(root.left,sum,True)
        if root.right:
            self._sumOfLeftLeaves(root.right,sum,False)
        return sum[0]

    def _sumOfLeftLeaves(self,node,sum,flag):
        if not node.left and not node.right and flag:
            sum[0] += node.val
            # print node.val
            return
        if node.left:
            self._sumOfLeftLeaves(node.left,sum,True)
        if node.right:
            self._sumOfLeftLeaves(node.right,sum,False)
