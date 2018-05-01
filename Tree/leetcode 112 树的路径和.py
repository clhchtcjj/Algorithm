# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 给定一棵树和sum，判断该树中是否存在一个和为sum的路径

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self._hasPathSum(root,sum)

    def _hasPathSum(self, root, sum):
        if root.left is None and root.right is None and sum == root.val:
            return True
        result = False
        if root.left:
            result = self._hasPathSum(root.left,sum-root.val)
            print result
        if result is False and root.right:
            # print 1
            result = self._hasPathSum(root.right,sum-root.val)
        return result

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        if root is None:
            return ans
        self._pathSum(root,sum,[],ans)
        return ans

    def _pathSum(self,node,sum,path,ans):
        if not node.left and not node.right and sum==node.val:
            ans.append(path+[node.val])
            return
        if node.left:
            self._pathSum(node.left,sum-node.val,path+[node.val],ans)
        if node.right:
            self._pathSum(node.right,sum-node.val,path+[node.val],ans)





