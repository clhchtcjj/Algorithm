# -*- coding: utf-8 -*-
__author__ = 'CLH'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        ans = [0]
        if not root:
            return ans[0]
        self.pathSumCore(root,sum,ans)
        return ans[0]

    # 前序遍历每个节点
    def pathSumCore(self,root,sum,ans):
        if not root:
            return
        self._pathSum(root,sum-root.val,ans)
        # print ans
        if root.left:
            self.pathSumCore(root.left,sum,ans)
        if root.right:
            self.pathSumCore(root.right,sum,ans)


    def _pathSum(self,node,sum,ans):
        if sum == 0:
            ans[0] += 1
        if not node:
            return
        if node.left:
            self._pathSum(node.left,sum-node.left.val,ans)
        if node.right:
            self._pathSum(node.right,sum-node.right.val,ans)


