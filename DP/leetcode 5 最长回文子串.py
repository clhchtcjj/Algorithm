# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 思路：由中间到两边找回文数

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = [""]
        for i in range(len(s)):
            self.extendPalindrome(s,i,i,ans)
            self.extendPalindrome(s,i,i+1,ans)
        return ans[0]
    def extendPalindrome(self,s,j, k, ans):
        while j >=0 and k <= len(s)-1 and s[j] == s[k]:
            j -= 1
            k += 1
        if k-j+1 > len(ans[0]):
            ans[0] = s[j:k+1]

