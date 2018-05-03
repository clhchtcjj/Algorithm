# -*- coding: utf-8 -*-
__author__ = 'CLH'

# Given a binary tree, return the tilt of the whole tree.
#
# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.
#
# The tilt of the whole tree is defined as the sum of all nodes' tilt.


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = []
        if not root:
            return 0
        self._findTilt(root,ans)
        return sum(ans)

    def _findTilt(self,node,ans):
        if not node:
            return 0
        left_sum = self._findTilt(node.left,ans)
        right_sum = self._findTilt(node.right,ans)
        curr = abs(left_sum-right_sum)
        ans.append(curr)
        return left_sum+right_sum+node.val