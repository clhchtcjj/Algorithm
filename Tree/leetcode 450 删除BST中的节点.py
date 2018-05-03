# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 思路：将删除的节点的值，替换为左子树最大值，或右子树最大值
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        return self._deleteNode(root,key)

    def _deleteNode(self,node,key):
        if node.val == key:
            if not node.left and not node.right: # 叶子节点
                node = None
            elif not node.right: # 没有右子树
                node = node.left
            elif not node.left:
                node = node.right
            else:
                # # 找到左子树的最大值
                # tmp = node.left
                # while tmp.right:
                #     tmp = tmp.right
                # print tmp.val
                # node.left = self._deleteNode(node.left,tmp.val)
                # node.val = tmp.val

                # 找到右子树的最小值
                tmp = node.right
                while tmp.left:
                    tmp = tmp.left
                node.right = self._deleteNode(node.right,tmp.val)
                node.val = tmp.val
        else:
            # 注意利用BST性质，剪枝
            if node.val > key and node.left:
                node.left = self._deleteNode(node.left,key)
            if node.val < key and node.right:
                node.right = self._deleteNode(node.right,key)
        return node
