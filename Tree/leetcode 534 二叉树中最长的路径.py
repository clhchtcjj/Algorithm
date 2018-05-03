# -*- coding:utf-8 -*-
__author__ = 'CLH'


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        _, ans = self._diameterOfBinaryTree(root)
        return ans

    def _diameterOfBinaryTree(self,node):
        if not node:
            return -1,-1
        left_path,left_path_root = self._diameterOfBinaryTree(node.left)
        right_path,right_path_root = self._diameterOfBinaryTree(node.right)
        path = left_path + right_path + 2
        # print node.val,max(left_path,right_path)+1,max(path,left_path_root,right_path_root)
        return max(left_path,right_path)+1,max(path,left_path_root,right_path_root)