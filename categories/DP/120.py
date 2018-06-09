# 解题思路：
# 定义状态： d[i,j] 走到trangle[i][j]处的最短路径之和
# 状态转移方程  d[i,j]  =  min(d[i-1][j],d[i-1][j-1])+triangle[i][j]  对于任何一点(i,j) 只有左上邻接和右上邻接两处可以达到 (i-1,j-1)和(i-1,j)
# 注意考虑 j为头和尾的情况下只有一条路可以选择
import copy


class Solution:
    def helper(self, triangle):

        d = copy.deepcopy(triangle)
        for i, l in enumerate(triangle):
            for j, e in enumerate(l):
                d[i][j] = triangle[i][j]
                if j == 0:
                    if i == 0:
                        continue
                    d[i][j] += d[i - 1][j]
                elif j == len(l) - 1:
                    d[i][j] += d[i - 1][j - 1]
                else:
                    d[i][j] += min(d[i - 1][j], d[i - 1][j - 1])

        return min(d[len(triangle) - 1])

    # 上面的问题可以简化成一位数组动态规划：
    # f[i]表示每一层的索引i处的最短路径，由下往上计算，可以在计算k层的时候把原先的k-1层的最短路径的替换掉。
    # 为什么可以这样 ：拿题目中的输入举例：由下往上走，在计算走到第三层的6的地方的时候，我们需要4->6和1->6谁比较小，
    # 计算完之后原先的f(0)处的即走到第四层的4因为不可能再被上一层需要了，所以可以被此时的f(0)即走到第三层的6处替代，此时的f(0)就是第3层的6处。
    def helper2(self, triangle):
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]


    # 从上往下走，是不能和上面这样替换掉的 因为上一层的最短路径可能会被下面的再次计算掉。这样是不行的  思考：为什么？
    def helper3(self, triangle):
        f = [0] * (len(triangle )+ 1)
        for row in triangle:
            for i in range(len(row)):
                f[i+1] = row[i]+min(f[i],f[i-1])

        return f[len(triangle)]

s = Solution()
t = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
    ]


print(s.helper(t))
print(s.helper2(t))
print(s.helper3(t))
