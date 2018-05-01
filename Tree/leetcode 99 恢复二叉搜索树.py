# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 问题:二叉树中有两个元素被换了位置，请恢复
# 思路：中序遍历，找到降序位置。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        lastnode=[None]
        first = [None]
        second = [None]
        self._recoverTree(root,lastnode,first,second)
        if first[0] and second[0]:
            first[0].val,second[0].val = second[0].val,first[0].val

    def _recoverTree(self,node,lastnode,first,second):
        if node is None:
            return
        if node.left:
            self._recoverTree(node.left,lastnode,first,second)
        if lastnode[0] and node.val < lastnode[0].val:
            if first[0] is None:
                first[0] = lastnode[0]
                second[0] = node
            else:
                second[0] = node
        if node.right:
            self._recoverTree(node.right,lastnode,first,second)