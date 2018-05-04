# -*- coding: utf-8 -*-
__author__ = 'CLH'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # print L,R
        if not root:
            return None
        if L > R:
            return
        if root.val <= L:
            left = None
        else:
            left = self.trimBST(root.left,L,R)
        if root.val >= R :
            right = None
        else:
            right = self.trimBST(root.right,L,R)

        if root.val < L or root.val > R:
            # print root.val
            if not right and not left:
                # print "-1"
                root = None
            elif not left:
                # print "-2"
                root = right
            elif not right:
                # print "-3"
                root = left
            else:
                # print "-4"
                node = left
                while node.right:
                    node = node.right
                root.val = node.val
                root.left = self.trimBST(left,node.val,node.val)
                root.right = right
        else:
            root.left = left
            root.right = right
        return root

        # 别人的解法
        # if not root:
        #     return None
			#
        # root.left = self.trimBST(root.left, L, R)
        # root.right = self.trimBST(root.right, L, R)
        #
        # if root.val < L:
        #     return root.right
        # if root.val > R:
        #     return root.left
        # return root