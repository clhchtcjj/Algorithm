# -*- coding:utf-8 -*-
__author__ = 'CLH'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            return self._isSubtree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def _isSubtree(self,s,t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            if s.val != t.val:
                return False
            else:
                return self._isSubtree(s.left,t.left) and self._isSubtree(s.right,t.right)

    # 序列化方法
    # def isSubtree(self, s, t):
    #     def string(root):
    #         return '(%d,%s,%s)' % (root.val, string(root.left), string(root.right)) if root else ''
    #     return string(t) in string(s)
