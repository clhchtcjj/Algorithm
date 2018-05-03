# -*- coding:utf-8 -*-
__author__ = 'CLH'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        q = [root]
        leftmost = None
        while len(q)!= 0:
            tmp_q = []
            leftmost = q[0].val
            for node in q:
                if node.left: tmp_q.append(node.left)
                if node.right: tmp_q.append(node.right)
            q = tmp_q

        return leftmost