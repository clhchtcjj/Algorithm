# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 二叉树的深度


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        1 当节点没有左右子树，则深度为1
        2 当节点有左子树没有右子树，则深度为左子树加1
        3 当节点有右子树没有左子树，则深度为右子树加1
        4 当节点有左右子树，则深度为左右子树的最大值加1
        """
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            return max(left,right)+1


    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        1 当节点没有左右子树，则深度为1
        2 当节点有左子树，没有右子树，则深度左子树深度加1
        3 当节点有右子树，没有左子树，则深度右子树深度加1
        4 当节点有左右子树，则深度为左右子树最小值加1
        """
        if not root:
            return 0
        elif not root.right and not root.left:
            return 1
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            if right == 0:
                return left+1
            if left == 0:
                return right+1
            else:
                return min(left,right)+1

