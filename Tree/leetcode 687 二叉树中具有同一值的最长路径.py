# -*- coding:utf-8 -*-
__author__ = 'CLH'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self._longestUnivaluePath(root)[1]

    def _longestUnivaluePath(self,node):
        if not node:
            return 0,0
        left_path, left_path_root = self._longestUnivaluePath(node.left)
        right_path, right_path_root = self._longestUnivaluePath(node.right)
        path = 0
        path_root = -1
        # print left_path, left_path_root,right_path,right_path_root
        if node.left and node.val == node.left.val:
            path = left_path + 1
        if node.right and node.val == node.right.val:
            if path < right_path + 1:
                path = right_path + 1
        if node.left and node.right and node.val == node.left.val and node.val == node.right.val:
            path_root = left_path+right_path+2
            # print path_root
        if path_root == -1:
            path_root = path
        path_root = max(left_path_root,right_path_root,path_root)
        # print path_root
        return path, path_root