# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 填充一个循环矩阵
# 思路：方阵，只要确定四个角的位置即可

class Solution(object):
    def __init__(self):
        self.matrix = None
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for j in range(n)]
        x = 0
        y = 0
        m,n = n,n
        num = 0
        while x < m and y < n:
            i = 0
            j = 0
            for j in range(y,n):
                num += 1
                matrix[x][j] = num
            for i in range(x+1,m):
                num += 1
                matrix[i][j] = num
            for j in range(j-1,y-1,-1):
                num += 1
                matrix[i][j] = num
            for i in range(m-2,x,-1):
                num += 1
                matrix[i][j] = num
            x += 1
            y += 1
            m -= 1
            n -= 1
        return matrix

    def fill(self,x,y,m,n,num):
        i = 0
        j = 0
        for j in range(y,n):
            num += 1
            self.matrix[x][j] = num
        for i in range(x+1,m):
            num += 1
            self.matrix[i][j] = num
        for j in range(j-1,y-1,-1):
            num += 1
            self.matrix[i][j] = num
        for i in range(m-2,x,-1):
            num += 1
            self.matrix[i][j] = num
        return num


if __name__ == "__main__":
    S = Solution()
    print(S.generateMatrix(4))