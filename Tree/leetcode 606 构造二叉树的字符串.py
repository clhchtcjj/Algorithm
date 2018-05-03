# -*- coding: utf-8 -*-
__author__ = 'CLH'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def string(root):
            if root:
                if root.left and root.right:
                    return "({}{}{})".format(root.val, string(root.left), string(root.right))
                elif not root.left and root.right:
                    return "({}{}{})".format(root.val, '()', string(root.right))
                elif not root.right and root.left:
                    return "({}{}{})".format(root.val, string(root.left), '')
                else:
                    return "({}{}{})".format(root.val, '', '')
        if not t:
            return ""
        return string(t)[1:-1]


