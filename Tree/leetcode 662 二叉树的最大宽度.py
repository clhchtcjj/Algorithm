# -*- coding: utf-8 -*-
__author__ = 'CLH'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        width = 0
        flag = True
        last_width = 1
        while len(q)!=0 and flag:
            tmp_q = []
            s, t = -1,-1
            flag = False
            for i in range(max(last_width)):
                node = q[i]
                if node is None:
                    tmp_q += [None,None]
                else:
                    flag = True
                    if s == -1:
                        s,t = i,i
                    else:
                        t = i
                        tmp_q += [node.left,node.right]
            q = tmp_q
            if width < t-s+1:
                width = t-s+1
            last_width = t-s+1
        return width

# class Solution:
#     def widthOfBinaryTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#
#         self.max = 1
#
#         def helper(root, height, offset, list):
#             if not root:
#                 return
#
#             if height >= len(list):
#                 list.append(offset)
#             else:
#                 self.max = max(self.max, offset - list[height] + 1)
#
#             helper(root.left, height + 1, 2*offset, list)
#             helper(root.right, height + 1, 2 * (offset) + 1, list)
#
#         helper(root, 0, 1,[])
#         return self.max
#