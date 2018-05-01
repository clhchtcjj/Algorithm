# -*- coding:utf-8 -*-
__author__ = 'CLH'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        lastnode = [None]
        self._flatten(root,lastnode)

    def _flatten(self,node,lastnode):
        if node is None:
            return
        tmpl = node.left
        tmpr = node.right
        # 保留上一个节点
        if lastnode[0]:
            lastnode[0].right = node
            # print str(lastnode.val)+"?"
            lastnode[0].left = None
        lastnode[0] = node
        # print lastnode[0].val
        self._flatten(tmpl,lastnode)
        self._flatten(tmpr,lastnode)
