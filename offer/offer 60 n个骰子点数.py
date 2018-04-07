# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 方法：dp
# f(n,s) = f(n-1,s-1)+f(n-1,s-2)+...+f(n-1,s-6)

class Solution(object):
    def getNSumCount(self,n,s):
        '''
        递归版本
        :param n:
        :param s:
        :return:
        '''
        if 6 * n < s or n < 1 or s < n:
            return 0
        if n == 1:
            return 1
        return self.getNSumCount(n-1,s-1) + self.getNSumCount(n-1,s-2) + self.getNSumCount(n-1,s-3)+\
                self.getNSumCount(n-1,s-4) + self.getNSumCount(n-1,s-5) + self.getNSumCount(n-1,s-6)

    def getNSumCountNotRecusion(self,n,s):
        '''
        非递归版本
        :param n:
        :param s:
        :return:
        '''
        num = [[0 for j in range(6*n+2)] for i in range(n+2)]
        for j in range(1,6*n+1):
            num[1][j] = 1
        for i in range(2,n+1):
            for j in range(6*n+1,0,-1):
                for k in range(1,7):
                    if j - k >0:
                        num[i][j] += num[i-1][j-k]
        return num[n][s]


if __name__ == "__main__":
    S = Solution()
    print(S.getNSumCountNotRecusion(3,6))