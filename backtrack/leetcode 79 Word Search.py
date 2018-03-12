__author__ = 'CLH'


'''
    Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell,
    where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once.
'''

class Solution:
    def __init__(self):
        self.board = [[]]
        self.pos = [[-1,0],[1,0],[0,-1],[0,1]]
        self.visited = [[]]

    def backtrack(self,row,col,word,n,m,k):
        if k == 1 and word[0] == self.board[row][col]:
            return True
        elif k == 1 and word[0] != self.board[row][col]:
            return False
        else:
            # has_pos = False
            if self.board[row][col] == word[0] and self.visited[row][col] == 0:
                self.visited[row][col] = 1
                for i, j in self.pos:
                    if 0 <= row+i and row+i < n and 0 <= col+j and col+j < m and self.visited[row+i][col+j] == 0:
                        # has_pos = True
                        if self.backtrack(row+i,col+j,word[1:],n,m,k-1):
                            return True
                self.visited[row][col] = 0
            # if has_pos == False:
            #     return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        n = len(board)
        m = len(board[0])
        self.visited = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.backtrack(i,j,word,n,m,len(word)):
                        return True
        return False

if __name__ == "__main__":
    S = Solution()
    board = [
              ['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']
            ]
    print(S.exist(board,"ABCB"))
    # board = [['a']]
    # print(S.exist(board,"a"))