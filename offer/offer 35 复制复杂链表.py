# -*- coding:utf-8 -*-
__author__ = 'CLH'

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    '''
    用hash方法
    '''
    def Clone(self, pHead):
        # write code here
        # 复制next
        if not pHead:
            return None
        head = RandomListNode(pHead.label)
        pnode = pHead
        cnode = head
        node_dict = {}
        node_dict[pnode] = cnode
        while pnode.next:
            cnode.next = RandomListNode(pnode.next.label)
            node_dict[pnode.next] = cnode.next
            pnode = pnode.next
            cnode = cnode.next
        # 复制random
        pnode = pHead
        while pnode:
            if pnode.random:
                node_dict[pnode].random = node_dict[pnode.random]
            pnode = pnode.next
        return head

if __name__ == "__main__":
    pHead = RandomListNode(1)
    pHead.next = RandomListNode(2)
    pHead.random = pHead.next
    S = Solution()
    head = S.Clone(pHead)
    print(head)




