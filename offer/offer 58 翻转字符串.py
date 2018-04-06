# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 翻转字符串

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s.strip()) == 0:
            return ""
        # 翻转句子
        s_list = list(s)
        n = len(s)
        s = 0; t = n-1
        while s <= t:
            s_list[s],s_list[t] = s_list[t],s_list[s]
            s+=1;t-=1
        s = ''.join(s_list)
        print(s)
        # 识别单词 翻转单词
        word_list = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and  s[j] == " ":
                j+=1
            i = j
            while j < len(s) and  s[j] != " ":
                j += 1
            if i < len(s) and s[i] != " ":
                word_list.append(s[i:j])
            i = j
        print(word_list)
        ans = []
        for word in word_list:
            word = word.strip()
            s = 0
            t = len(word)-1
            word_list = list(word)
            while s <= t:
                word_list[s],word_list[t] = word_list[t],word_list[s]
                s+=1;t-=1
            ans.append(''.join(word_list).strip()+" ")
        return ''.join(ans).strip()

    def reverseString(self,s,k):
        if type(s) == str:
            s_list = list(s)
        s = 0
        t = k-1
        for i in range(3):
            if i == 0:
                s = 0; t = k-1
            if i == 1:
                s = k; t = len(s_list)-1
            if i == 2:
                s = 0; t = len(s_list)-1
            while s <= t:
                s_list[s],s_list[t] = s_list[t],s_list[s]
                s += 1
                t -= 1
        return ''.join(s_list)



if __name__ == "__main__":
    S = Solution()
    print(S.reverseString("abcdefg",3))

