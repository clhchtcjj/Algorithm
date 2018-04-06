# -*- coding:utf-8 -*-
__author__ = 'CLH'

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".

# 考虑重复的情况
import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        need : < 0 表示队列中包含的，
        """
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
if __name__ == "__main__":
    S = Solution()
    print(S.minWindow("bcaba","ab"))





