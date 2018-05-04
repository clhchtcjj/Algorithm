# -*- coding:utf-8 -*-
__author__ = 'CLH'

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        # 计算层数
        def countlevel(node):
            if not node:
                return 0
            q = [node]
            cnt = 0
            while len(q) != 0:
                tmp_q = []
                cnt += 1
                for node in q:
                    if node.left: tmp_q.append(node.left)
                    if node.right: tmp_q.append(node.right)
                q = tmp_q
            return cnt
        level = countlevel(root)
        string = [""] * (2 ** level -1) # 获得list
        ans = [list(string) for _ in range(level)]
        self._printTree(root,0,len(string)-1,0,ans)
        return ans

    # 递归完成
    def _printTree(self,node,s,t,h,ans):
        mid = (s+t) // 2
        if mid >= 0:
            ans[h][mid] = str(node.val)
            if node.left:
                self._printTree(node.left,s,mid-1,h+1,ans)
            if node.right:
                self._printTree(node.right,mid+1,t,h+1,ans)





