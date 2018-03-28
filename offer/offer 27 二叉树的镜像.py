# -*- coding:utf-8 -*-
__author__ = 'CLH'

import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点

    def Mirror(self, root):
        '''
        在原始树上修改
        :param root:
        :return:
        '''
        # write code here
        if root:
            tmp = root.right
            root.right = root.left
            root.left = tmp
            self.Mirror(root.left)
            self.Mirror(root.right)


    def get_Mirror(self,root):
        '''
        新建一棵二叉树
        :param root:
        :return:
        '''
        mirror_root = None
        if root:
            mirror_root = TreeNode(root.val)
            mirror_root.left = self.get_Mirror(root.right)
            mirror_root.right = self.get_Mirror(root.left)
        return mirror_root

    def printTree(self,root):
        '''
        按层遍历并换行
        :param root:
        :return:
        '''
        queue = Queue.Queue()
        queue.put(root)
        last = root
        nlast = root
        while not queue.empty():
            node = queue.get()
            if node.left:
                queue.put(node.left)
                nlast = node.left
            if node.right:
                queue.put(node.right)
                nlast = node.right
            if last == node:
                print "{}\n".format(node.val),
                last = nlast
            else:
                print "{} ".format(node.val),

        print
if __name__ == "__main__":
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right = TreeNode(10)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)
    S = Solution()
    S.printTree(root)
    root = S.get_Mirror(root)
    # S.Mirror(root)
    S.printTree(root)




