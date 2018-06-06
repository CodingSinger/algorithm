import copy


class Solution:
    def helper(self, grid):

        # 和62的思路差不多 也是需要一个数组计算每一个点的时候的最优路径长度
        p = copy.deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    p[i][j] += p[i][j-1]
                elif j == 0:
                    p[i][j] += p[i - 1][j]
                else:
                    p[i][j] += min(p[i - 1][j], p[i][j - 1])
        return p[len(grid) - 1][len(grid[0]) - 1]


s = Solution()
grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]
print(s.helper(grid))
