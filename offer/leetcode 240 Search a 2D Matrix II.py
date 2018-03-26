__author__ = 'CLH'

class Solution():
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m < 1:
            return False
        n = len(matrix[0])
        if n < 1:
            return False
        i,j = 0, n-1
        while(1):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                if j-1<0:
                    return False
                else:
                    j = j -1
                continue
            else:
                if i + 1 > m-1:
                    return False
                else:
                    i = i+1
                continue

if __name__ == "__main__":
    # matrix = [
    #           [1,   4,  7, 11, 15],
    #           [2,   5,  8, 12, 19],
    #           [3,   6,  9, 16, 22],
    #           [10, 13, 14, 17, 24],
    #           [18, 21, 23, 26, 30]
    #         ]
    matrix = [[]]
    S = Solution()
    print(S.searchMatrix(matrix,0))



