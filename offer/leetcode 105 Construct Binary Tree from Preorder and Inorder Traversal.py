__author__ = 'CLH'

# 根据前序后序构建二叉树
# Definition for a binary tree node.
import Queue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def buildTree(self, preorder, inorder):
    #     """
    #     :type preorder: List[int]
    #     :type inorder: List[int]
    #     :rtype: TreeNode
    #     """
    #     if len(preorder) == 0:
    #         return None
    #     root = TreeNode(preorder[0])
    #     if len(preorder)== 1:
    #         return root
    #     index = inorder.index(preorder[0])
    #     left_inorder = inorder[:index]
    #     right_inorder = inorder[index+1:]
    #     left_preorder = preorder[1:1+len(left_inorder)]
    #     right_preorder = preorder[1+len(left_inorder):]
    #     root.left = self.buildTree(left_preorder,left_inorder)
    #     root.right = self.buildTree(right_preorder,right_inorder)
    #     return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder:
            root = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:index+1],inorder[0:index])
            root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
            return root

    def print_preorder(self,node):
        if node:
            print(node.val)
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_inorder(self,node):
        if node:
            self.print_inorder(node.left)
            print(node.val)
            self.print_inorder(node.right)

    def print_postorder(self,node):
        if node:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node.val)

    # 按层打印
    def print_tree(self,node):
        queue = Queue.Queue()
        queue.put(node)
        pstart = node
        pend = node
        while not queue.empty():
            curr = queue.get()
            pend = curr
            if pstart == pend:
                print "{}".format(curr.val)
                pstart = pend.right
            else:
                print "{} ".format(curr.val),
            if curr.left:
                queue.put(curr.left)
            if curr.right:
                queue.put(curr.right)

if __name__ == "__main__":
    preorder = [1,2,4,5,3,6,7]
    inorder = [4,2,5,1,6,3,7]
    S = Solution()
    tree = S.buildTree(preorder,inorder)
    # print(tree)
    print("##")
    S.print_inorder(tree)
    print("##")
    S.print_postorder(tree)
    print("##")
    S.print_tree(tree)