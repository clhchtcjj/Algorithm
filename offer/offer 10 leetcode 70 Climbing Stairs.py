# -- coding: utf-8 --
__author__ = 'CLH'

# 爬楼梯 
# f(n) = f(n-1)+f(n-2)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0,1]
        for i in range(2,n):
        	ans.append(ans[i-1] + ans[i-2])
        return ans[n-1]

if __name__ == "__main__":
	S = Solution()
	print(S.climbStairs(3))