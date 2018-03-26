# -- coding: utf-8 --
__author__ = 'CLH'

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = []

        for i in range(0,num+1):
            n = i
            cnt = 0
            while n!=0:
                cnt+=1
                n &= (n-1)
            ans.append(cnt)
        return ans

if __name__ == "__main__":
    S = Solution()
    print(S.countBits(5))