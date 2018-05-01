# -*- coding: utf-8 -*-
__author__ = 'CLH'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        maxsum = [None]
        self._maxPathSum(root,maxsum)
        return maxsum[0]

    def _maxPathSum(self,root,maxsum):
        if not root:
            return None
        currVal = root.val
        lmaxSum = rmaxSum = None
        if root.left:
            lmaxSum = self._maxPathSum(root.left,maxsum)
        if root.right:
            rmaxSum = self._maxPathSum(root.right,maxsum)
        if lmaxSum and lmaxSum > 0:
            currVal += lmaxSum
        if rmaxSum and rmaxSum > 0:
            currVal += rmaxSum
        if currVal > maxsum[0]:
            maxsum[0] = currVal
        # 注意返回值
        return max(root.val,root + lmaxSum, root+rmaxSum)

