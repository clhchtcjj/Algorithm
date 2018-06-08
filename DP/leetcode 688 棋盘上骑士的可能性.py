# -*- coding: utf-8 -*-
__author__ = 'CLH'


# 既然算概率，那么就要求分子、分母两个。分母的求法为8的次方
# 分母可以用动规完成

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if N == 0:
            return 0
        if K == 0:
            return 1
        dp = [[1 for _ in range(N)] for _ in range(N)]
        dirs = [[-1,-2],[-2,-1],[-1,2],[2,-1],[1,2],[2,1],[-2,1],[1,-2]]
        for k in range(K):
            tmp = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for dir in dirs:
                        x = i + dir[0]
                        y = j + dir[1]
                        if x < 0 or x >=N or y < 0 or y >= N:
                            continue
                        tmp[i][j] += dp[x][y]
            dp = tmp
        return dp[r][c] * 1.0  / pow(8,K)

if __name__ == "__main__":
    S = Solution()
    print(S.knightProbability(3, 2, 0, 0))