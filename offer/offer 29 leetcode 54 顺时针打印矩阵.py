# -*- coding:utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def __init__(self):
        self.ans= []
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        x = 0
        y = 0
        while x < m and y < n:
            self.printMatrix(matrix,x,y,m,n)
            m -= 1
            n -= 1
            x += 1
            y += 1
        return self.ans
    def printMatrix(self,matrix,x,y,m,n):
        i = 0
        j = 0
        if m < 0:
            return
        # 一行的情况
        if x+1 == m:
            for j in range(y,n):
                # print "{} ".format(matrix[x][j]),
                self.ans.append(matrix[x][j])
            return
        # 一列的情况
        if y+1 == n:
            for i in range(x,m):
                # print "{} ".format(matrix[i][j]),
                self.ans.append(matrix[i][y])
            return
        else:
            for j in range(y,n):
                # print "{} ".format(matrix[x][j]),
                self.ans.append(matrix[x][j])
            for i in range(x+1,m):
                # print "{} ".format(matrix[i][j]),
                self.ans.append(matrix[i][j])
            for j in range(j-1,y-1,-1):
                # print "{} ".format(matrix[i][j]),
                self.ans.append(matrix[i][j])
            for i in range(m-2,x,-1):
                # print "{} ".format(matrix[i][j]),
                self.ans.append(matrix[i][j])


if __name__ == "__main__":
    matrix = [
                 [ 1 ],
                 [ 4],
                 [ 7],
                 [ 16],
                 [ 21]
            ]
    S = Solution()
    print(S.spiralOrder(matrix))
