# -*- coding:utf-8 -*-
__author__ = 'CLH'


class Soultion():
    def BF(self,S,T):
        n = len(S)
        m = len(T)
        if m == 0 or n == 0:
            return -1
        i = j = 0
        while i < n and j < m:
            if S[i] != T[j]:
                i = i-j+1
                j = 0
            else:
                i += 1
                j += 1
        if j == m:
            return i-j
        else:
            return -1

if __name__ == "__main__":
    S = Soultion()
    print(S.BF("abc",""))
