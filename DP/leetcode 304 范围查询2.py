# -*- coding:utf-8 -*-
__author__ = 'CLH'


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        n = len(matrix)
        self.n = n
        if n > 0:
            m = len(matrix[0])
            self.dp_1 = [[0 for _ in range(m)] for _ in range(n)]
            # print self.dp_1
            for i in range(n):
                self.dp_1[i][0] = matrix[i][0]
                for j in range(1, m):
                    self.dp_1[i][j] = matrix[i][j] + self.dp_1[i][j-1]
            for j in range(m):
                for i in range(1, n):
                    self.dp_1[i][j] += self.dp_1[i-1][j]
            # print(self.dp_1)




    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.n == 0:
            return None
        if row1 == 0 and col1 == 0:
            return self.dp_1[row2][col2]
        elif row1 == 0:
            return self.dp_1[row2][col2] - self.dp_1[row2][col1-1]
        elif col1 == 0:
            return self.dp_1[row2][col2] - self.dp_1[row1-1][col2]
        else:
            return self.dp_1[row2][col2] - self.dp_1[row1-1][col2] - self.dp_1[row2][col1-1]+ self.dp_1[row1-1][col1-1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == "__main__":
    matrix = [[-4,-5]]

    obj = NumMatrix(matrix)
    param_1 = obj.sumRegion(0,1,0,1)
    print(param_1)