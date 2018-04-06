# -*- coding: utf-8 -*-
__author__ = 'CLH'


# 判断一棵树是不是平衡二叉树
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        判断一颗树是不是二叉平衡树需要等左右子树的深度都计算出来 => 为避免重复遍历，可以采用后序遍历
        """
        depth = [0]
        return self.__isBalanced(root,depth)

    def __isBalanced(self,root,depth):
        if not root:
            depth[0] = 0
            return True
        else:
            depth_l = [0]
            depth_r = [0]
            if self.__isBalanced(root.right,depth_l) and self.__isBalanced(root.left,depth_r):
                diff = abs(depth_l[0] - depth_r[0])
                if diff <=1:
                    depth[0] += max(depth_l[0],depth_r[0])+1
                    return True
            return False


