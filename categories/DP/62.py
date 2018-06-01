class Solution:
    def helper(self, m, n):
        path = [[0 for i in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    path[i][j] = 1 #地图最左端或者最上端 只有一种选择能到达该地 即一直往下或者一直往右
                else:
                    path[i][j] += path[i - 1][j] + path[i][j - 1] #否则往下和往右的走法相加

        return path[n - 1][m - 1]


s = Solution()
print(s.helper(3, 2))
