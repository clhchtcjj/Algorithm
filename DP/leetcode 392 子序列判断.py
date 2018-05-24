# -*- coding:utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        if n > m:
            return False
        if n == 0:
            return True
        if m == 0:
            return False
        i = 0
        j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == n:
            return True
        else:
            return False