# -*- coding: utf-8 -*-
__author__ = 'CLH'



class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        n = len(pairs)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = 1
        self.quick_sort(pairs,0,n-1)
        print(pairs)
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = (max(dp[j]+1,dp[i]))
                    break
                # elif pairs[j][0] > pairs[i][1]:
                #     dp[i] = max(dp[j]+1,dp[i])
                else:
                    dp[i] = max(dp[i],1)
        return max(dp)

    def quick_sort(self,pairs,s,t):
        if s < t:
            pivot = self.partition(pairs,s,t)
            self.quick_sort(pairs,s, pivot-1)
            self.quick_sort(pairs,pivot+1,t)

    def partition(self,pairs,s,t):
        pivot = pairs[s]
        while s < t:
            while s < t and pivot[0] <= pairs[t][0]:
                t -= 1
            pairs[s] = pairs[t]
            while s < t and pivot[0] > pairs[s][0]:
                s += 1
            pairs[t] = pairs[s]
        pairs[s] = pivot
        return s




if __name__ == "__main__":
    S = Solution()
    print(S.findLongestChain([[9,10],[-4,9],[-5,6],[-5,9],[8,9]]))