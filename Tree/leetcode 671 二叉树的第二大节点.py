# -*- coding: utf-8 -*-

__author__ = 'CLH'



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        ans = [-1]
        self._findSecondMinimumValue(root,ans)
        return ans[0]

    def _findSecondMinimumValue(self,node,ans):
        if not node:
            return -1
        if ans[0] != -1:
            return
        left = self._findSecondMinimumValue(node.left,ans)
        right = self._findSecondMinimumValue(node.right,ans)
        if left!=-1 and left > node.val:
            ans[0] = node.val
        if right != -1 and right > node.val:
            ans[0] = node.val
        return node
