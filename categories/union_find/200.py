class Solution:


    #该题和130其实差不太多，主要目的是 以相连的为一组，查看一共分布了几组，首先会想到，从边界开始搜索，如果为1，则对其四周进行搜索，如果四周元素也有为1的，则对该元素也进行递归深搜
    #需要注意的是这种连通题需要将已经走过的元素设置为另一个数值，以避免重复对其进行搜索。
    def helper(self, grid):

        row, col = len(grid), len(grid[0]) if grid else 0

        def dfs(i, j):

            # if grid[i][j] == last:
            #     return

            if j + 1 <= col - 1 and grid[i][j + 1] == '1':
                grid[i][j + 1] = grid[i][j]
                dfs(i, j + 1)
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                grid[i][j - 1] = grid[i][j]
                dfs(i, j - 1)
            if i + 1 <= row - 1 and grid[i + 1][j] == '1':
                grid[i + 1][j] = grid[i][j]
                dfs(i + 1, j)

            if i - 1 >= 0 and grid[i - 1][j] == '1':
                grid[i - 1][j] = grid[i][j]
                dfs(i - 1, j)

        cur = 1
        for i, rows in enumerate(grid):
            for j, e in enumerate(rows):
                if e == '1':
                    cur += 1
                    grid[i][j] = str(cur)
                    # 往下和往右深搜
                    dfs(i, j)

        return cur - 1


s = Solution()
grid2 = [["1", "1", "1", "1", "0"],
         ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "0"]]
grid = [[1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]]

grid1 = [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1]]

grid3 = [["1", "1", "1"],
         ["0", "1", "0"],
         ["1", "1", "1"]]

grid4 = [["1", "0", "1", "1", "1"],
         ["1", "0", "1", "0", "1"],
         ["1", "0", "1", "0", "1"]]

grid5 = [["1", "1", "1", "1", "0"],
         ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "0"]]

print(s.helper(grid4))
