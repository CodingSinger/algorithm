class Solution:



    # 大体思路和62题差不多 只是需要验证当前路径是不是障碍 如果是障碍的话则使path[i][j] = 0，表示走到此处是无路可走的，
    # 但要注意 障碍的坐标 i,j在i= 0或者j =0的情况下应该需要传递，obstacleGrid[0][j] 都为0，或者obstacleGrid[i][0]都为0
    def helper(self, obstacleGrid):

        path = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):

                if obstacleGrid[i][j] == 1:
                    if i == 0 and j + 1 < len(obstacleGrid[0]): #i == 0和j ==0的情况需要特殊处理 ，避免进入下一个判断
                        obstacleGrid[i][j + 1] = 1
                    if j == 0 and i + 1 < len(obstacleGrid):
                        obstacleGrid[i + 1][j] = 1
                    continue
                elif i == 0 or j == 0:

                    path[i][j] = 1
                else:
                    path[i][j] = path[i - 1][j] + path[i][j - 1]

        return path[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
s = Solution()
print(s.helper([[0,0,0],
               [0,1,0],
                [0,0,0]]))
