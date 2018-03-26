__author__ = 'CLH'


class Solution():
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m <= 0:
            return False
        n = len(matrix[0])
        if n <= 0:
            return False
        for i in range(m):
            start,end = matrix[i][0],matrix[i][-1]
            if start > target:
                return False
            elif end < target:
                continue
            else:
                for j in range(0,n):
                    return self.binarySearch(0,n,matrix[i],target)
        return False

    def  binarySearch(self,start,end,nums,target):
        if start > end:
            return False
        mid = int((start + end) / 2)
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return self.binarySearch(start,mid-1,nums,target)
        else:
            return self.binarySearch(mid+1,end,nums,target)




if __name__ == "__main__":
#     matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
    matrix = []
    S = Solution()
    print(S.searchMatrix(matrix,0))
    