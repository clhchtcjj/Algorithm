# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 栈的压入、弹出序列
# 申请一个栈，来模拟弹出、压入情况，当栈顶与弹出序列同，即弹出，否则继续压栈

class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        i = 0
        tmp_stack = []
        j = 0
        while i < len(popV) and j <= len(pushV):
            if len(tmp_stack) == 0:
                if j == len(pushV):
                    return False
                tmp_stack.append(pushV[j])
                j += 1
                continue
            elif tmp_stack[-1] != popV[i]:
                if j == len(pushV):
                    return False
                tmp_stack.append(pushV[j])
                j += 1
                continue
            elif tmp_stack[-1] == popV[i]:
                tmp_stack.pop()
                i += 1
        if i == j and len(tmp_stack) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    S = Solution()
    print(S.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))
