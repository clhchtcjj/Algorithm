# -*- coding:utf-8 -*-
__author__ = 'CLH'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pre,curr1,curr2 = None,pHead1,pHead2
        while curr1 and curr2:
            if curr1.val > curr2.val:
                if pre:
                    pre.next = curr2
                    curr2_next = curr2.next
                    curr2.next = curr1
                    curr2 = curr2_next
                    pre = pre.next
                else:
                    # 头
                    pHead1 = curr2
                    curr2_next = curr2.next
                    curr2.next = curr1
                    curr2 = curr2_next
                    pre = pHead1
            else:
                pre,curr1 = curr1,curr1.next

        # 处理pHead2剩余的节点
        if not curr1:
            if pre:
                pre.next = curr2
            else:
                pHead1 = curr2
        return pHead1

    def printList(self,head):
        node = head
        while node:
            print "{} ".format(node.val),
            node = node.next
        print

if __name__ == "__main__":
    head1 = ListNode(1)
    node = head1
    for i in [2,5,7,8]:
        node.next = ListNode(i)
        node = node.next

    head2 = ListNode(1)
    node = head2
    for i in [3,4,6]:
        node.next = ListNode(i)
        node = node.next

    S = Solution()
    # head1 = None
    head = S.Merge(head1,head2)
    S.printList(head)





