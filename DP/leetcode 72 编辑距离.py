# -*- coding:utf-8 -*-
__author__ = 'CLH'

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)
        n = len(word1)+1
        m = len(word2)+1
        dp = [[0 for j in range(m)] for i in range(n)]
        dp[0][0] = 0
        # if word1[0] =
        for i in range(1,n):
            dp[i][0] = dp[i-1][0]+1
        for j in range(1,m):
            dp[0][j] = dp[0][j-1]+1
        for i in range(1,n):
            for j in range(1,m):
                # print(i,j)
                if word1[i-1] == word2[j-1]:
                    # print(i-2,j-2)
                    dp[i][j] = dp[i-1][j-1]
                else:#             插入            删除       替换
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[-1][-1]


if __name__ == "__main__":
    S = Solution()
    print(S.minDistance("ab","bc"))
