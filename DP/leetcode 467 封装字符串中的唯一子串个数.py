# -*- coding: utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        # # 超时解法
        # if p == "":
        #     return 0
        # s = 0
        # substring_set = set()
        # substring_set.add(p[0])
        # for i in range(1,len(p)):
        #     if (ord(p[i-1])-95) % 26 == (ord(p[i])-96) % 26:
        #         # print (ord(p[i-1])-96) % 26, (ord(p[i])-96) % 26 - 1
        #         for j in range(s,i):
        #             substring_set.add(p[j:i+1])
        #             substring_set.add(p[i])
        #     else:
        #         substring_set.add(p[i])
        #         s = i
        # return len(substring_set)

        # 记录以26个字母为结尾的连续字符串的长度，然后逐个相加即可
        # 我们看abcd这个字符串，以d结尾的子字符串有abcd, bcd, cd, d，
        # 那么我们可以发现bcd或者cd这些以d结尾的字符串的子字符串都包含在abcd中，
        # 那么我们知道以某个字符结束的最大字符串包含其他以该字符结束的字符串的所有子字符串
        if p == "":
            return 0
        dp = [1]
        lens_dict = {p[0]:1}
        for i in range(1,len(p)):
            if (ord(p[i-1])-95) % 26 == (ord(p[i])-96) % 26:
                lens = dp[i-1] + 1
                dp.append(lens)
            else:
                lens = 1
                dp.append(lens)
            if lens_dict.get(p[i]) is None:
                lens_dict[p[i]] = lens
            else:
                lens_dict[p[i]] = max(lens_dict[p[i]],lens)
        ans = 0
        for key in lens_dict.keys():
            ans += lens_dict[key]
        return ans


if __name__ == "__main__":
    S = Solution()
    print(S.findSubstringInWraproundString("uvwxyzabcdefg"))