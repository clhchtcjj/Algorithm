__author__ = 'CLH'

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

        for lens in range(len(rightmosts)):

