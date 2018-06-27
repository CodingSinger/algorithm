

# 思路很简单，
# 如果直接找被包围的O,从一个'O'开始搜索判断是不是会到达边界，将会非常麻烦，因为需要保存路径上的每个'O'，如果到达边界就放弃这片区域的所有值，否则将其变为'X'。
# 有一种更为聪明的做法就是我们找到不被包围的O并做上记号，怎样的是不被包围的O呢，我们从四个边界开始搜索，边界的O肯定是不被包围的，因此我们将其做上记号为1，然后我们搜索该O的四周是否也存在O,如果存在则表示该O也不会被包围。直到
# 遍历整个数组
# 所以算法是从四个边界出发，用DFS算法将从边界开始的'O'的区域都变成另外一个临时的值，这样做完之后剩下的‘O’将会是被包围的，然后将其变为‘X’，再将临时的值变为'O'即可。
class Solution:
    def helper(self, board):
        h = len(board)
        w = len(board[0])

        def DFS(i, j):
            if board[i][j] == 'O':
                board[i][j] = '1'
            if i > 1 and board[i - 1][j] == 'O':
                DFS(i - 1, j)
            if i + 1 < h and board[i + 1][j] == 'O':
                DFS(i + 1, j)
            if j + 1 < w and board[i][j + 1] == 'O':
                DFS(i, j + 1)
            if j > 1 and board[i][j - 1] == 'O':
                DFS(i, j - 1)

        for i in range(h):
            if board[i][0] == 'O':
                DFS(i, 0)
        for i in range(h):
            if board[i][w - 1] == 'O':
                DFS(i, w - 1)
        for i in range(w):
            if board[h - 1][i] == 'O':
                DFS(h - 1, i)
        for i in range(w):
            if board[0][i] == 'O':
                DFS(0, i)
        for i in range(h):
            for j in range(w):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        return board
s = Solution()
board = [["X","O","X","O","X","O"],
         ["O","X","O","X","O","X"],
         ["X","O","X","O","X","O"],
         ["O","X","O","X","O","X"]]


print(s.helper(board))
