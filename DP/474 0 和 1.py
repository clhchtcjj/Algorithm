# -*- coding:utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        lens = len(strs)
        def count(str):
            zeros = 0
            ones = 0
            for ch in str:
                if ch == "1":
                    ones += 1
                else:
                    zeros += 1
            return zeros,ones
        # 0-1背包问题，用dp[i][j][k]表示前i个字符串在0的个数不超过j，1的个数不超过k时
        # 最多选能选取的字符串的个数。
        # 状态转移：dp[i][j][k] = dp[i-1][j-cnt0][k-cnt1] + 1 选字符串i;
        #           dp[i][j][k] = dp[i-1][j][k] 不选字符串i
        # 空间可以复用,从后向前遍历

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for str in strs:
            cnt0,cnt1 = count(str)
            for i in range(m, cnt0-1,-1):
                for j in range(n, cnt1-1, -1):
                    dp[i][j] = max(dp[i][j],dp[i-cnt0][j-cnt1]+1)
        return dp[m][n]






if __name__ == "__main__":
    S = Solution()
    print S.findMaxForm(["10", "0001", "111001", "1", "0"],5,3)