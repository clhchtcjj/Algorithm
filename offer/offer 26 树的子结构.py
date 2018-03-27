# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 树的问题，一般都考虑采用递归的方法，先找根节点，然后判断是否为子树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = True
            if result:
                result = self.isSubtree(pRoot1,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right,pRoot2)
        return result

    def isSubtree(self,pRoot1,pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSubtree(pRoot1.left,pRoot2.left) and self.isSubtree(pRoot1.right,pRoot2.right)



