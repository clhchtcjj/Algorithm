# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 思路：遍历树，以值构造数组，对数组进行处理

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def get_nodes(node):
            return [node.val] + get_nodes(node.left) + get_nodes(node.right) if node else []
        nodes = get_nodes(root)
        for i in xrange(len(nodes)):
            if k - nodes[i] in nodes[i+1:]:
                return True
        return False

