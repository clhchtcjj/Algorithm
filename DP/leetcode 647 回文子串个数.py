# -*- coding: utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        ans = 0
        for i in range(n):
            ans += 1
            left = i-1
            right = i+1
            while left>=0 and right<n and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1

            left = i
            right = i+1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1

        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.countSubstrings("aaa"))