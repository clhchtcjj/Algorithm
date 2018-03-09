__author__ = 'CLH'

import operator

# 实现字典树
class Node(object):
    def __init__(self,c=None,word=None):
        self.c = c
        self.word = word
        self.childs = []

class Trie(object):
    def __init__(self):
        self.root = Node()

    def find(self,node,c):
        '''
        查找插入位置
        :param node:
        :param c:
        :return: 位置
        '''
        childs = node.childs
        _len = len(childs)
        if _len == 0:
            return -1
        for i in range(_len):
            if childs[i].c == c:
                return i
        return -1

    def add(self,word):
        node =self.root
        for c in word:
            pos = self.find(node,c)
            if pos < 0:
                node.childs.append(Node(c))
                node.childs = sorted(node.childs, key = lambda child:child.c)
                pos = self.find(node,c)
            node = node.childs[pos]
        node.word = word

    def search(self,word):
        node  = self.root
        for c in word:
            pos = self.find(node,c)
            if pos < 0:
                return False
            else:
                node = node.childs[pos]
        return node.word == word
#
class Solution():
    def __init__(self):
        self.trie = Trie()
        self.board = None
        self.visited = None
        self.max_len = 0
        self.ans = []
        self.words = []
        self.dir = [[-1,0],[1,0],[0,-1],[0,1]]

    # def is_a_solution(self,word):
    #     return self.trie.search(word)

    def backtrack(self,node,word,row,col,n,m):
        if node.word == word:
            if word not in self.ans:
                self.ans.append(word)
        if row < 0 or row > n-1 or col < 0 or col > m-1 or self.visited[row][col]:
            return
        else:
            pos = self.trie.find(node,self.board[row][col])
            if pos == -1:
                return
            else:
                node = node.childs[pos]
                word += node.c
                self.visited[row][col] = 1
                for dir in self.dir:
                    self.backtrack(node,word,row+dir[0],col+dir[1],n,m)
                self.visited[row][col] = 0
                # if self.is_a_solution(_word):
                #     return

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.board = board
        n = len(board)
        m = len(board[0])
        self.visited = [[0 for i in range(m)] for i in range(n)]
        for word in words:
            self.trie.add(word)
        for i in range(n):
            for j in range(m):
                self.backtrack(self.trie.root,"",i,j,n,m)
        return self.ans
#     # 简单解法
#     def findWords(self, board, words):
#         trie = {}
#         for w in words:
#             t = trie
#             for c in w:
#                 if c not in t:
#                     t[c] = {}
#                 t = t[c]
#             t['#'] = '#'
#         res = []
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 self.find(board, i, j, trie, '', res)
#         return list(set(res))
#
#     def find(self, board, i, j, trie, path, res):
#         if '#' in trie:
#             res.append(path)
#         if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] not in trie:
#             return
#         tmp = board[i][j]
#         board[i][j] ="@"
#         self.find(board, i+1, j, trie[tmp], path+tmp, res)
#         self.find(board, i, j+1, trie[tmp], path+tmp, res)
#         self.find(board, i-1, j, trie[tmp], path+tmp, res)
#         self.find(board, i, j-1, trie[tmp], path+tmp, res)
#         board[i][j] = tmp

if __name__ == "__main__":
    S = Solution()
    # board = [ ['o','a','a','n'],
    #           ['e','t','a','e'],
    #           ['i','h','k','r'],
    #           ['i','f','l','v']]
    # words = ["oath","pea","eat","rain"]
    board = [["a","b"],["a","a"]]
    words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
    print(S.findWords(board,words))

