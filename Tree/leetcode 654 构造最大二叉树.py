# -*- coding: utf-8 -*-
__author__ = 'CLH'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        return self._constructMaximumBinaryTree(nums,0,len(nums)-1)

    def _constructMaximumBinaryTree(self,num,s,t):
        # print s,t
        if s > t:
            return None
        # 找最大值
        max_num = num[s]
        max_id = s
        for i in range(s+1,t+1):
            if num[i] > max_num:
                max_num = num[i]
                max_id = i
        node = TreeNode(max_num)
        node.left = self._constructMaximumBinaryTree(num,s,max_id-1)
        node.right = self._constructMaximumBinaryTree(num,max_id+1,t)
        return node

