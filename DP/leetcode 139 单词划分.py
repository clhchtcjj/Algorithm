# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 问题：判断能否将字符串切分为字典中的单词
# 思路：dp[i][j]表示已下标i字母开头的其后j+1个字符能否构成单词，如果不能直接构成，考虑一分为二，遍历切分点k。
# 剪枝：只有当dp[i][k-1]能构成单词，才需要考虑dp[i+k][j-k]是否可以构单词

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        rightmosts, words = [0], set(wordDict)
        for i in range(1, len(s) + 1):
            for last_index in rightmosts:
                if s[last_index:i] in words:
                    rightmosts.append(i)
                    if i == len(s): return True
                    break
        return False

