# -*- coding:utf-8 -*-
__author__ = 'CLH'

# Definition for a binary tree node.
import math
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        return self._sortedArrayToBST(nums,0,len(nums)-1)

    def _sortedArrayToBST(self,nums,s,t):
        if s < t:
            return None
        mid = int(math.floor((s+t) / 2.0))
        print mid
        root = TreeNode(nums[mid])
        root.left = self._sortedArrayToBST(nums,s,mid-1)
        root.right = self._sortedArrayToBST(nums,mid+1,t)
        return root       
