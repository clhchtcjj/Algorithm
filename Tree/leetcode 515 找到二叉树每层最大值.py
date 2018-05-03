# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 思路：层次遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q = [root]
        ans = []
        while len(q) != 0:
            tmp_q = []
            current_max = None
            for node in q:
                if current_max is None or current_max < node.val:
                    current_max = node.val
                if node.left: tmp_q.append(node.left)
                if node.right: tmp_q.append(node.right)
            ans.append(current_max)
            q = tmp_q
        return ans
