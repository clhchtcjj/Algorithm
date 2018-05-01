# -*- coding:utf-8 -*-
__author__ = 'CLH'


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        result = False
        result = self.isSameTree(p.letf,q.left)
        if result:
            if p.val == q.val:
                result = True
            else:
                result = False
        if result:
            result = self.isSameTree(p.right,q.right)


        return result


