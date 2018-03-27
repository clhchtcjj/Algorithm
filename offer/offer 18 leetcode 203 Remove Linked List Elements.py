# -- coding:utf-8 --
__author__ = 'CLH'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        '''考虑删除链表中指定元素'''
        '''考虑删除头结点的情况'''
        pre, curr = None,head
        while curr:
            if curr.val == val:
                if pre:
                    pre.next = curr.next
                    curr = curr.next
                else:
                    head = curr.next
                    curr = curr.next
            else:
                pre, curr = curr, curr.next
        return head

    def deleteNodeO1(self,head,node):
        '''
        :param head:
        :param node:
        :return:
        '''
        '''删除链表中指定节点，O(1)时间'''''
        # 删除头结点,需要特殊处理头指针
        if node == head:
            head = head.next
        # 删除尾节点，它后面没有节点
        elif node.next == None:
            tmp = head
            while tmp.next != node:
                tmp = tmp.next
            tmp.next = node.next
        else:
            node.val = node.next.val
            node.next = node.next.next
        return head

    def printLink(self,head):
        node = head
        while node:
            print "{} ".format(node.val),
            node = node.next
        print


if __name__ == "__main__":
    head = ListNode(1)
    node = head
    for i in [2,3,4,5,6,7,8]:
        node.next = ListNode(i)
        node = node.next
    node = head
    while node.next!=None:
        node = node.next
    S = Solution()
    S.printLink(head)
    head = S.deleteNodeO1(head,node)
    S.printLink(head)
    print("ok")

