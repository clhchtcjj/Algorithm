# -*- coding:utf-8 -*-
__author__ = 'CLH'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def helper(root, dict, output):
            if not root:
                return "n"

            left = helper(root.left, dict, output)
            right = helper(root.right, dict, output)
            val = str(root.val) + left + right
            if val in dict:
                if not dict[val]:
                    output.append(root)
                    dict[val] = True
            else:
                dict[val] = False
            return val

        output = []
        helper(root, {}, output)
        return output





